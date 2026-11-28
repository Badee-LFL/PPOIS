import unittest
from src.models import Medicine, Batch, Client, Order, OrderLine
from src.exceptions import *

class TestLab2Pharma(unittest.TestCase):
    def setUp(self):
        self.medicine = Medicine("Aspirin", "500mg", False)
        self.medicine.set_price(10.0)
        self.batch = Batch("B001", self.medicine, 100, "2026-12-31")
        self.medicine.attach_batch(self.batch)
        self.client = Client("City Hospital")

    def test_stock_and_batch(self):
        self.assertEqual(self.medicine.calculate_available_stock(), 100)
        self.batch.deduct_quantity(20)
        self.assertEqual(self.medicine.calculate_available_stock(), 80)
        with self.assertRaises(InsufficientStockException):
            self.batch.deduct_quantity(100)

    def test_order_flow(self):
        order = Order(1, self.client)
        order.add_line(OrderLine(self.medicine, 5)) 
        self.assertEqual(order.calculate_total(), 50.0)
        order.submit()
        self.assertEqual(order.state, "Submitted")
        
    def test_invalid_order(self):
        order = Order(2, self.client)
        order.submit()
        with self.assertRaises(InvalidOrderStateException):
            order.add_line(OrderLine(self.medicine, 5))

if __name__ == '__main__':
    unittest.main()