import os

dummy_classes = {
    "manufacturer": "Manufacturer", "supplier": "Supplier", "contract": "Contract",
    "cold_storage": "ColdStorageZone", "doctor": "Doctor", "pharmacist": "Pharmacist",
    "prescription": "Prescription", "sales_manager": "SalesManager", "logistics_manager": "LogisticsManager",
    "driver": "Driver", "employee": "Employee", "invoice": "Invoice", "payment": "Payment",
    "discount": "Discount", "price_list": "PriceList", "return_request": "ReturnRequest",
    "refund_service": "RefundService", "vehicle": "Vehicle", "route": "Route", "shipment": "Shipment",
    "recall": "Recall", "quality_control": "QualityControl", "audit_record": "AuditRecord",
    "temperature_log": "TemperatureLog", "barcode": "Barcode", "serial_number": "SerialNumber",
    "batch_tracker": "BatchTracker", "inventory_analyzer": "InventoryAnalyzer", 
    "demand_forecaster": "DemandForecaster", "reorder_planner": "ReorderPlanner", "report": "Report",
    "report_generator": "ReportGenerator", "notification_service": "NotificationService",
    "payment_gateway": "PaymentGateway", "loyalty_program": "LoyaltyProgram", "complaint": "Complaint",
    "insurance": "Insurance", "license": "License", "regulation": "Regulation",
    "contact_info": "ContactInfo", "address": "Address", "company": "Company", "department": "Department",
    "user": "User", "warehouse": "Warehouse"
}

for filename, classname in dummy_classes.items():
    with open(f"src/models/{filename}.py", "w") as f:
        f.write(f"class {classname}:\n")
        f.write(f"    def __init__(self, name: str):\n")
        f.write(f"        self.name = name\n")
        f.write(f"    def get_name(self):\n")
        f.write(f"        return self.name\n")

print("Generated 45 model files.")