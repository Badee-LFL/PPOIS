from exceptions import (
    InvalidMedicineDataException,
    InsufficientStockException,
    InvalidOrderStateException,
    ColdChainViolationException,
    WarehouseCapacityException
)

class Manufacturer:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self._medicines = []

    def add_medicine(self, medicine):
        self._medicines.append(medicine)

class Medicine:
    def __init__(self, name: str, dosage: str, manufacturer: Manufacturer):
        if not name or not dosage:
            raise InvalidMedicineDataException("Name and dosage are mandatory.")
        self.name = name
        self.dosage = dosage
        self.manufacturer = manufacturer
        self.price = 0.0
        self._batches = []

    def set_price(self, price: float):
        if price < 0:
            raise InvalidMedicineDataException("Price cannot be negative.")
        self.price = price

    def attach_batch(self, batch):
        self._batches.append(batch)

    def get_total_available(self) -> int:
        return sum(b.quantity for b in self._batches if not b.is_expired)

class Batch:
    def __init__(self, batch_number: str, medicine: Medicine, quantity: int, is_expired: bool = False):
        self.batch_number = batch_number
        self.medicine = medicine
        self.quantity = quantity
        self.is_expired = is_expired

    def deduct_quantity(self, amount: int):
        if amount > self.quantity:
            raise InsufficientStockException("Not enough in this batch.")
        self.quantity -= amount

class Warehouse:
    def __init__(self, warehouse_id: str, capacity: int):
        self.warehouse_id = warehouse_id
        self.capacity = capacity
        self._current_stock = 0

    def add_stock(self, amount: int):
        if self._current_stock + amount > self.capacity:
            raise WarehouseCapacityException("Exceeds warehouse capacity.")
        self._current_stock += amount

class ColdStorageZone:
    def __init__(self, zone_id: str, min_temp: float, max_temp: float):
        self.zone_id = zone_id
        self.min_temp = min_temp
        self.max_temp = max_temp

    def check_temperature(self, temp: float):
        if temp < self.min_temp or temp > self.max_temp:
            raise ColdChainViolationException(f"Temp {temp} out of bounds!")

class Client:
    def __init__(self, client_id: int, name: str):
        self.client_id = client_id
        self.name = name
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

class OrderLine:
    def __init__(self, medicine: Medicine, quantity: int):
        self.medicine = medicine
        self.quantity = quantity

    def calculate_subtotal(self) -> float:
        return self.medicine.price * self.quantity

class Order:
    def __init__(self, order_id: int, client: Client):
        self.order_id = order_id
        self.client = client
        self._lines = []
        self._state = "draft"

    def add_line(self, line: OrderLine):
        if self._state != "draft":
            raise InvalidOrderStateException("Cannot modify a submitted order.")
        self._lines.append(line)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self._lines)

    def submit(self):
        for line in self._lines:
            if line.medicine.get_total_available() < line.quantity:
                raise InsufficientStockException(f"Not enough stock for {line.medicine.name}")
        self._state = "submitted"

class Invoice:
    def __init__(self, invoice_id: int, order: Order):
        self.invoice_id = invoice_id
        self.order = order
        self.total_amount = order.calculate_total()
        self.is_paid = False

    def mark_as_paid(self):
        self.is_paid = True

class Payment:
    def __init__(self, payment_id: int, invoice: Invoice, amount: float):
        self.payment_id = payment_id
        self.invoice = invoice
        self.amount = amount

    def process_payment(self):
        if self.amount < self.invoice.total_amount:
            raise ValueError("Insufficient payment amount")
        self.invoice.mark_as_paid()

class Prescription:
    def __init__(self, prescription_id: int, doctor_name: str, medicine: Medicine):
        self.prescription_id = prescription_id
        self.doctor_name = doctor_name
        self.medicine = medicine
        self.is_valid = True

    def invalidate(self):
        self.is_valid = False