from .exceptions import *

class Manufacturer:
    def __init__(self, name: str, country: str, license_number: str):
        self.name = name
        self.country = country
        self.license_number = license_number
        self.medicines = []
    def add_medicine(self, medicine):
        self.medicines.append(medicine)

class Medicine:
    def __init__(self, name: str, dosage: str, form: str, requires_prescription: bool):
        if not name or not dosage:
            raise InvalidMedicineDataException("Name and dosage required.")
        self.name = name
        self.dosage = dosage
        self.form = form
        self.requires_prescription = requires_prescription
        self.price = 0.0
        self.batches = []
    def set_price(self, price: float):
        if price < 0:
            raise InvalidMedicineDataException("Price cannot be negative.")
        self.price = price
    def attach_batch(self, batch):
        self.batches.append(batch)
    def calculate_available_stock(self) -> int:
        return sum(b.quantity for b in self.batches if not b.is_expired)

class Batch:
    def __init__(self, batch_number: str, medicine: Medicine, quantity: int, expiry_date: str):
        self.batch_number = batch_number
        self.medicine = medicine
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.is_expired = False
    def mark_expired(self):
        self.is_expired = True
    def deduct_quantity(self, amount: int):
        if amount > self.quantity:
            raise InsufficientStockException("Not enough in batch.")
        self.quantity -= amount

class Warehouse:
    def __init__(self, location: str, capacity: int):
        self.location = location
        self.capacity = capacity
        self.current_stock = 0
    def add_stock(self, amount: int):
        if self.current_stock + amount > self.capacity:
            raise WarehouseCapacityException("Capacity exceeded.")
        self.current_stock += amount
    def remove_stock(self, amount: int):
        self.current_stock = max(0, self.current_stock - amount)

class ColdStorageZone:
    def __init__(self, zone_id: str, min_temp: float, max_temp: float):
        self.zone_id = zone_id
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.current_temp = min_temp
    def monitor_temperature(self, temp: float):
        self.current_temp = temp
        if temp < self.min_temp or temp > self.max_temp:
            raise ColdChainViolationException("Temperature out of bounds!")

class Supplier:
    def __init__(self, name: str, contact_email: str):
        self.name = name
        self.contact_email = contact_email
        self.is_approved = False
        self.batches = []
    def approve(self):
        self.is_approved = True
    def supply_batch(self, batch):
        if not self.is_approved:
            raise SupplierNotApprovedException("Supplier is not approved.")
        self.batches.append(batch)

class Contract:
    def __init__(self, contract_id: str, supplier: Supplier, duration_months: int):
        self.contract_id = contract_id
        self.supplier = supplier
        self.duration_months = duration_months
        self.is_active = True
    def terminate(self):
        self.is_active = False

class Client:
    def __init__(self, name: str, client_type: str):
        self.name = name
        self.client_type = client_type
        self.orders = []
    def place_order(self, order):
        self.orders.append(order)

class Pharmacy(Client):
    def __init__(self, name: str, license: str):
        super().__init__(name, "Pharmacy")
        self.license = license
        self.inventory = []
    def request_restock(self, medicine: Medicine, qty: int):
        self.inventory.append({"medicine": medicine, "qty": qty})

class Hospital(Client):
    def __init__(self, name: str, beds: int):
        super().__init__(name, "Hospital")
        self.beds = beds
    def request_emergency_supply(self, medicine: Medicine):
        return f"Emergency request for {medicine.name}"

class Doctor:
    def __init__(self, name: str, license_number: str):
        self.name = name
        self.license_number = license_number
    def write_prescription(self, medicine: Medicine, patient_name: str):
        return Prescription(patient_name, self, medicine)

class Pharmacist:
    def __init__(self, name: str, license: str):
        self.name = name
        self.license = license
    def dispense(self, prescription):
        if not prescription.is_valid:
            raise PrescriptionRequiredException("Invalid prescription.")
        prescription.is_dispensed = True

class SalesManager:
    def __init__(self, name: str, target: float):
        self.name = name
        self.target = target
        self.sales = 0.0
    def record_sale(self, amount: float):
        self.sales += amount
    def calculate_commission(self) -> float:
        return self.sales * 0.05

class LogisticsManager:
    def __init__(self, name: str):
        self.name = name
        self.shipments = []
    def assign_shipment(self, shipment):
        self.shipments.append(shipment)

class Driver:
    def __init__(self, name: str, license: str):
        self.name = name
        self.license = license
        self.location = "Warehouse"
    def update_location(self, loc: str):
        self.location = loc

class Employee:
    def __init__(self, name: str, role: str, salary: float):
        self.name = name
        self.role = role
        self.salary = salary
    def give_raise(self, percent: float):
        self.salary += self.salary * (percent / 100)

class Prescription:
    def __init__(self, patient_name: str, doctor: Doctor, medicine: Medicine):
        self.patient_name = patient_name
        self.doctor = doctor
        self.medicine = medicine
        self.is_valid = True
        self.is_dispensed = False
    def invalidate(self):
        self.is_valid = False

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
        self.lines = []
        self.state = "Draft"
    def add_line(self, line: OrderLine):
        if self.state != "Draft":
            raise InvalidOrderStateException("Order already submitted.")
        self.lines.append(line)
    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.lines)
    def submit(self):
        for line in self.lines:
            if line.medicine.calculate_available_stock() < line.quantity:
                raise InsufficientStockException("Not enough stock.")
        self.state = "Submitted"

class Invoice:
    def __init__(self, invoice_id: str, order: Order):
        self.invoice_id = invoice_id
        self.order = order
        self.total = order.calculate_total()
        self.is_paid = False
    def mark_paid(self):
        self.is_paid = True

class Payment:
    def __init__(self, amount: float, method: str):
        self.amount = amount
        self.method = method
        self.status = "Pending"
    def process(self, invoice: Invoice):
        if self.amount < invoice.total:
            raise PaymentFailedException("Insufficient funds.")
        self.status = "Completed"
        invoice.mark_paid()

class Discount:
    def __init__(self, percentage: float, valid_until: str):
        self.percentage = percentage
        self.valid_until = valid_until
    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)

class PriceList:
    def __init__(self, name: str):
        self.name = name
        self.entries = {}
    def add_entry(self, medicine: Medicine, price: float):
        self.entries[medicine.name] = price

class ReturnRequest:
    def __init__(self, order: Order, reason: str):
        self.order = order
        self.reason = reason
        self.status = "Pending"
    def approve(self):
        self.status = "Approved"

class RefundService:
    def __init__(self):
        self.refunds = []
    def process_refund(self, payment: Payment, amount: float):
        self.refunds.append({"payment": payment, "amount": amount})
        payment.status = "Refunded"

class Vehicle:
    def __init__(self, plate: str, capacity: float, is_refrigerated: bool):
        self.plate = plate
        self.capacity = capacity
        self.is_refrigerated = is_refrigerated
    def check_capacity(self, weight: float):
        if weight > self.capacity:
            raise ValueError("Vehicle overloaded.")

class Route:
    def __init__(self, start: str, end: str, distance_km: float):
        self.start = start
        self.end = end
        self.distance_km = distance_km

class Shipment:
    def __init__(self, order: Order, vehicle: Vehicle, driver: Driver, route: Route):
        self.order = order
        self.vehicle = vehicle
        self.driver = driver
        self.route = route
        self.status = "Preparing"
    def dispatch(self):
        self.status = "In Transit"
        self.driver.update_location(self.route.start)
    def deliver(self):
        self.status = "Delivered"
        self.driver.update_location(self.route.end)

class Recall:
    def __init__(self, batch: Batch, reason: str):
        self.batch = batch
        self.reason = reason
        self.is_active = True
    def execute(self):
        self.batch.mark_expired()
        self.is_active = False

class QualityControl:
    def __init__(self, inspector: str):
        self.inspector = inspector
        self.tests_passed = 0
    def run_test(self, passed: bool):
        if passed:
            self.tests_passed += 1

class AuditRecord:
    def __init__(self, auditor: str, date: str):
        self.auditor = auditor
        self.date = date
        self.findings = []
    def log_finding(self, finding: str):
        self.findings.append(finding)

class TemperatureLog:
    def __init__(self, zone: ColdStorageZone):
        self.zone = zone
        self.logs = []
    def log_temperature(self, temp: float):
        self.zone.monitor_temperature(temp)
        self.logs.append(temp)

class Barcode:
    def __init__(self, code: str):
        self.code = code
    def scan(self) -> str:
        return f"Scanned {self.code}"

class SerialNumber:
    def __init__(self, number: str):
        self.number = number
        self.is_invalidated = False
    def invalidate(self):
        self.is_invalidated = True

class BatchTracker:
    def __init__(self, batch: Batch):
        self.batch = batch
        self.location = "Manufacturer"
    def update_location(self, loc: str):
        self.location = loc

class InventoryAnalyzer:
    def __init__(self, warehouse: Warehouse):
        self.warehouse = warehouse
    def check_low_stock(self, threshold: int):
        if self.warehouse.current_stock < threshold:
            return "Low Stock Alert"

class DemandForecaster:
    def __init__(self, medicine: Medicine):
        self.medicine = medicine
    def forecast_next_month(self) -> int:
        return len(self.medicine.batches) * 100

class ReorderPlanner:
    def __init__(self, analyzer: InventoryAnalyzer):
        self.analyzer = analyzer
        self.pending_orders = []
    def create_reorder(self, qty: int):
        self.pending_orders.append(qty)

class Report:
    def __init__(self, title: str, data: dict):
        self.title = title
        self.data = data
    def format_json(self) -> str:
        return f'{{"title": "{self.title}", "data": {self.data}}}'

class ReportGenerator:
    def __init__(self):
        self.reports = []
    def generate_sales_report(self, manager: SalesManager):
        report = Report("Sales Report", {"manager": manager.name, "sales": manager.sales})
        self.reports.append(report)
        return report

class NotificationService:
    def __init__(self):
        self.messages = []
    def send_email(self, email: str, msg: str):
        self.messages.append(f"Email to {email}: {msg}")

class PaymentGateway:
    def __init__(self, gateway_name: str):
        self.gateway_name = gateway_name
    def authorize(self, amount: float) -> bool:
        return amount > 0

class LoyaltyProgram:
    def __init__(self, client: Client):
        self.client = client
        self.points = 0
    def add_points(self, amount: float):
        self.points += int(amount)

class Complaint:
    def __init__(self, client: Client, text: str):
        self.client = client
        self.text = text
        self.is_resolved = False
    def resolve(self):
        self.is_resolved = True

class Insurance:
    def __init__(self, provider: str, coverage: float):
        self.provider = provider
        self.coverage = coverage
    def file_claim(self, amount: float) -> float:
        return min(amount, self.coverage)

class License:
    def __init__(self, number: str, expiry_date: str):
        self.number = number
        self.expiry_date = expiry_date
    def check_valid(self, current_date: str) -> bool:
        return current_date <= self.expiry_date

class Regulation:
    def __init__(self, name: str):
        self.name = name
        self.rules = []
    def add_rule(self, rule: str):
        self.rules.append(rule)

class ContactInfo:
    def __init__(self, email: str, phone: str):
        self.email = email
        self.phone = phone
    def update_email(self, new_email: str):
        self.email = new_email

class Address:
    def __init__(self, street: str, city: str, zip_code: str):
        self.street = street
        self.city = city
        self.zip_code = zip_code
    def format_address(self) -> str:
        return f"{self.street}, {self.city}, {self.zip_code}"

class Company:
    def __init__(self, name: str, tax_id: str):
        self.name = name
        self.tax_id = tax_id
        self.departments = []
    def add_department(self, dept):
        self.departments.append(dept)

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
    def hire_employee(self, employee: Employee):
        self.employees.append(employee)