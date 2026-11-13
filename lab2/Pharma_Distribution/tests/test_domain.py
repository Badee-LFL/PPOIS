import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from domain import Manufacturer, Medicine, Batch, Order, OrderLine, Client, ColdStorageZone
from exceptions import InvalidMedicineDataException, InsufficientStockException, ColdChainViolationException

@pytest.fixture
def sample_medicine():
    mfg = Manufacturer("Test", "US")
    med = Medicine("TestMed", "100mg", mfg)
    med.set_price(10.0)
    return med

def test_invalid_medicine_data():
    with pytest.raises(InvalidMedicineDataException):
        Medicine("", "500mg", Manufacturer("Test", "US"))

def test_negative_price(sample_medicine):
    with pytest.raises(InvalidMedicineDataException):
        sample_medicine.set_price(-5.0)

def test_insufficient_stock(sample_medicine):
    client = Client(1, "Test Client")
    order = Order(1, client)
    order.add_line(OrderLine(sample_medicine, 10))
    
    with pytest.raises(InsufficientStockException):
        order.submit()

def test_cold_chain_violation():
    zone = ColdStorageZone("Z1", 2.0, 8.0)
    with pytest.raises(ColdChainViolationException):
        zone.check_temperature(15.0)