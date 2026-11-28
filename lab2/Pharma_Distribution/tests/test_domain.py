import unittest
from src.models import *
from src.exceptions import *

class TestLab2Pharma(unittest.TestCase):
    def setUp(self):
        self.medicine = Medicine("Aspirin", "500mg", False)
        self.medicine.set_price(10.0)
        self.batch = Batch("B001", self.medicine, 100, "2026-12-31")
        self.medicine.attach_batch(self.batch)

    def test_stock(self):
        self.assertEqual(self.medicine.calculate_available_stock(), 100)
        self.batch.deduct_quantity(20)
        self.assertEqual(self.medicine.calculate_available_stock(), 80)
        with self.assertRaises(InsufficientStockException):
            self.batch.deduct_quantity(100)

    def test_order(self):
        order = Order(1, "Client")
        order.add_line(OrderLine(self.medicine, 5)) 
        order.submit()
        invoice = Invoice("INV-1", order)
        payment = Payment(50.0, "Card")
        payment.process(invoice)
        self.assertTrue(invoice.is_paid)

    def test_remaining_classes(self):
        wh = Warehouse("Berlin", 1000)
        wh.add_stock(500)
        sup = Supplier("Global", "test@test.com")
        sup.approve()
        sup.supply_batch(self.batch)
        
        ColdStorageZone("Z1", 2.0, 8.0).monitor_temperature(5.0)
        Pharmacy("P", "L").request_restock(self.medicine, 10)
        Hospital("H", 10).request_emergency_supply(self.medicine)
        Doctor("D", "L").write_prescription(self.medicine, "P")
        Pharmacist("P", "L").dispense(Prescription("P", Doctor("D", "L"), self.medicine))
        
        sm = SalesManager("S", 100); sm.record_sale(10); sm.calculate_commission()
        LogisticsManager("L").assign_shipment(Shipment(Order(3, "C"), Vehicle("V", 100, True), Driver("D", "L"), Route("A", "B", 10)))
        
        Recall(self.batch, "R").execute()
        QualityControl("Q").run_test(True)
        AuditRecord("A", "2026").log_finding("F")
        TemperatureLog(ColdStorageZone("Z", 0, 10)).log_temperature(5)
        
        Barcode("123").scan()
        SerialNumber("1").invalidate()
        BatchTracker(self.batch).update_location("L")
        InventoryAnalyzer(wh).check_low_stock(1000)
        DemandForecaster(self.medicine).forecast_next_month()
        ReorderPlanner(InventoryAnalyzer(wh)).create_reorder(10)
        
        ReportGenerator().generate_sales_report(sm)
        NotificationService().send_email("e", "m")
        PaymentGateway("G").authorize(100)
        LoyaltyProgram("C").add_points(100)
        Complaint("C", "T").resolve()
        Insurance("I", 1000).file_claim(500)
        License("L", "2026").check_valid("2026")
        Regulation("R").add_rule("Rule")
        ContactInfo("e", "p").update_email("n")
        Address("s", "c", "z").format_address()
        
        comp = Company("C", "T")
        dept = Department("D")
        comp.add_department(dept)
        dept.hire_employee(Employee("E", "R", 100))
        
        Discount(10, "2026").apply(100)
        PriceList("P").add_entry(self.medicine, 10)
        ReturnRequest(Order(4, "C"), "R").approve()
        RefundService().process_refund(Payment(100, "C"), 50)
        Contract("C", sup, 12).terminate()
        Manufacturer("M", "C").add_medicine(self.medicine)
        User("U", "R").update_name("N")

if __name__ == '__main__':
    unittest.main()