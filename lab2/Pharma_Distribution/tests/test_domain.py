import unittest
from src.domain import *
from src.exceptions import (
    InvalidMedicineDataException, InsufficientStockException,
    InvalidOrderStateException, ColdChainViolationException,
    WarehouseCapacityException, PrescriptionRequiredException,
    PaymentFailedException, SupplierNotApprovedException
)

class TestLab2Pharma(unittest.TestCase):
    
    def setUp(self):
        self.mfg = Manufacturer("PharmaCorp", "DE", "LIC-123")
        self.medicine = Medicine("Aspirin", "500mg", "Tablet", False)
        self.medicine.set_price(10.0)
        self.batch = Batch("B001", self.medicine, 100, "2026-12-31")
        self.medicine.attach_batch(self.batch)
        self.client = Pharmacy("City Pharmacy", "PH-123")

    def test_invalid_medicine_data(self):
        with self.assertRaises(InvalidMedicineDataException):
            Medicine("", "500mg", "Tablet", False)
            
    def test_negative_price(self):
        with self.assertRaises(InvalidMedicineDataException):
            self.medicine.set_price(-5.0)

    def test_batch_deduction_and_stock(self):
        self.assertEqual(self.medicine.calculate_available_stock(), 100)
        self.batch.deduct_quantity(20)
        self.assertEqual(self.medicine.calculate_available_stock(), 80)
        with self.assertRaises(InsufficientStockException):
            self.batch.deduct_quantity(100)

    def test_warehouse_capacity(self):
        wh = Warehouse("Berlin", 500)
        wh.add_stock(400)
        self.assertEqual(wh.current_stock, 400)
        with self.assertRaises(WarehouseCapacityException):
            wh.add_stock(200)

    def test_cold_chain_violation(self):
        zone = ColdStorageZone("Z1", 2.0, 8.0)
        zone.monitor_temperature(5.0)
        with self.assertRaises(ColdChainViolationException):
            zone.monitor_temperature(10.0)

    def test_supplier_approval(self):
        supplier = Supplier("GlobalMeds", "contact@global.com")
        with self.assertRaises(SupplierNotApprovedException):
            supplier.supply_batch(self.batch)
        supplier.approve()
        supplier.supply_batch(self.batch)
        self.assertEqual(len(supplier.batches), 1)

    def test_prescription_dispense(self):
        doc = Doctor("Dr. Smith", "DOC-123")
        script = doc.write_prescription(self.medicine, "John Doe")
        pharmacist = Pharmacist("Jane", "PH-999")
        pharmacist.dispense(script)
        self.assertTrue(script.is_dispensed)
        script.invalidate()
        with self.assertRaises(PrescriptionRequiredException):
            pharmacist.dispense(script)

    def test_sales_commission_and_raise(self):
        manager = SalesManager("Alice", 10000.0)
        manager.record_sale(5000.0)
        self.assertEqual(manager.calculate_commission(), 250.0)
        emp = Employee("Bob", "Sales", 3000.0)
        emp.give_raise(10)
        self.assertEqual(emp.salary, 3300.0)

    def test_order_flow_and_payment(self):
        order = Order(1, self.client)
        line = OrderLine(self.medicine, 5) 
        order.add_line(line)
        self.assertEqual(order.calculate_total(), 50.0)
        order.submit()
        self.assertEqual(order.state, "Submitted")
        with self.assertRaises(InvalidOrderStateException):
            order.add_line(OrderLine(self.medicine, 2))

        invoice = Invoice("INV-1", order)
        self.assertFalse(invoice.is_paid)
        payment_fail = Payment(40.0, "Credit Card")
        with self.assertRaises(PaymentFailedException):
            payment_fail.process(invoice)
            
        payment_ok = Payment(50.0, "Credit Card")
        payment_ok.process(invoice)
        self.assertTrue(invoice.is_paid)
        self.assertEqual(payment_ok.status, "Completed")

    def test_discounts_and_returns(self):
        disc = Discount(10.0, "2026-01-01")
        self.assertEqual(disc.apply(100.0), 90.0)
        order = Order(2, self.client)
        ret = ReturnRequest(order, "Damaged")
        ret.approve()
        self.assertEqual(ret.status, "Approved")

    def test_shipment_logistics(self):
        driver = Driver("Sam", "LIC-1")
        vehicle = Vehicle("ABC-123", 1000.0, False)
        route = Route("Berlin", "Munich", 500.0)
        order = Order(3, self.client)
        shipment = Shipment(order, vehicle, driver, route)
        shipment.dispatch()
        self.assertEqual(shipment.status, "In Transit")
        self.assertEqual(driver.location, "Berlin")
        shipment.deliver()
        self.assertEqual(shipment.status, "Delivered")
        self.assertEqual(driver.location, "Munich")
        with self.assertRaises(ValueError):
            vehicle.check_capacity(2000.0)

    def test_recalls_and_quality(self):
        recall = Recall(self.batch, "Contamination")
        recall.execute()
        self.assertTrue(self.batch.is_expired)
        self.assertFalse(recall.is_active)
        qc = QualityControl("Inspector 1")
        qc.run_test(True)
        qc.run_test(False)
        qc.run_test(True)
        self.assertEqual(qc.tests_passed, 2)

    def test_inventory_analytics(self):
        wh = Warehouse("Berlin", 1000)
        wh.add_stock(50)
        analyzer = InventoryAnalyzer(wh)
        self.assertEqual(analyzer.check_low_stock(100), "Low Stock Alert")
        self.assertIsNone(analyzer.check_low_stock(20))

    def test_loyalty_and_departments(self):
        loyalty = LoyaltyProgram(self.client)
        loyalty.add_points(150.50)
        self.assertEqual(loyalty.points, 150)
        company = Company("PharmaCorp", "TAX-1")
        dept = Department("Sales")
        company.add_department(dept)
        dept.hire_employee(Employee("Charlie", "Rep", 2000))
        self.assertEqual(len(dept.employees), 1)

if __name__ == "__main__":
    unittest.main()