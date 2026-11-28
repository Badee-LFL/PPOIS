# Design of Intelligent Systems Software - Lab Assignments

This repository contains the lab assignments for the "Design of Intelligent Systems Software" course. 

## Repository Structure
- `lab1/` — OOP Fundamentals (Vector, Polynomial)
- `lab2/` — Large-Scale OOP Project (Pharma Distribution)
- `lab3/` — Large-Scale OOP Project (Online Learning Platform)

## Build & Test
The project builds and tests from the console without an IDE. A CI/CD pipeline is configured via GitHub Actions.

To run tests and check coverage locally:
```bash
# Example for Lab 2
cd lab2/Pharma_Distribution
python -m coverage run tests/testPolynomial.py
for report : 
python -m coverage report -m

# Lab Assignment #1: OOP Fundamentals (Vector & Polynomial)

## Domain Description
Lab 1 focuses on the fundamental principles of Object-Oriented Programming (OOP) in Python. The project consists of two independent mathematical data types: a 3D Vector and a Single-Variable Polynomial. Both implementations demonstrate encapsulation, operator overloading (via magic methods), deep copying, and strict separation of concerns between the domain logic and the console user interface.

## 1. 3D Vector (`3D_Vector`)
**Class:** `Vector3D`

### Features & Encapsulation
- **Coordinates**: Encapsulated as private attributes (`__x`, `__y`, `__z`) and exposed via read-only `@property` getters.
- **Validation**: The `__convert_coordinate` method ensures all inputs are finite real numbers (rejecting `bool` and `NaN`).
- **Copying**: Implements a `copy()` method to return an independent instance with the same coordinates.

### Operator Overloading (Magic Methods)
- **Arithmetic**: `__add__` (`+`), `__sub__` (`-`), `__mul__` (scalar multiplication or cross product), `__rmul__` (scalar on left), `__truediv__` (`/`), and `__neg__` (unary minus).
- **Equality & Comparison**: `__eq__` (uses `math.isclose` for floating-point precision), `__lt__`, `__le__`, `__gt__`, `__ge__` (compares vectors by their Euclidean length).
- **String Representation**: `__str__` outputs a readable `(x, y, z)` format, while `__repr__` outputs a reconstructable `Vector3D(x, y, z)` format.
- **Factory Method**: `from_string(text)` parses comma-separated values into a vector.

## 2. Single-Variable Polynomial (`Polynomial`)
**Class:** `Polynomial`

### Features & Encapsulation
- **Coefficients**: Stored as an immutable tuple in ascending power order (e.g., `[1, 2, 3]` means \(1 + 2x + 3x^2\)).
- **Normalization**: Automatically strips trailing zeros to maintain the true degree.
- **Validation**: Rejects non-real or infinite coefficients.

### Operator Overloading (Magic Methods)
- **Arithmetic**: `__add__` (`+`), `__sub__` (`-`), `__mul__` (`*` for scalar or polynomial multiplication), `__truediv__` (`/` for scalar division or exact polynomial long division), and `__neg__` (unary minus).
- **Evaluation**: Implements `__call__` and `evaluate(x)` using Horner's method for efficient computation.
- **Indexing**: `__getitem__` allows retrieving the coefficient for a specific power.
- **Equality**: `__eq__` and `__hash__` compare normalized coefficient sequences.
- **String Representation**: `__str__` outputs `[1, 2, 3]`, and `__repr__` outputs `Polynomial(1.0, 2.0, 3.0)`.

## Exceptions and Error Handling
Both classes implement **Fail-Fast** error handling:
- **`TypeError`**: Raised when invalid types (e.g., strings or booleans) are passed.
- **`ValueError`**: Raised for non-finite numbers (e.g., `NaN`), negative prices, or non-exact polynomial division.
- **`ZeroDivisionError`**: Raised when attempting to divide a vector or polynomial by zero.
- **`IndexError`**: Raised when accessing a negative polynomial power.

## CLI Interface
Both variants include a console menu (`src/main.py`) that demonstrates the domain logic without polluting the class implementations:
- **Vector Menu**: Add, subtract, calculate dot/cross products, find lengths, and calculate the cosine angle.
- **Polynomial Menu**: Add, subtract, multiply, divide, evaluate at a point, and find degrees.

## Documentation (pdoc)
The code is fully documented using the standard Python `pdoc` generator. The generated HTML documentation is available in the `docs/` folder for both variants, providing a clean API reference for all classes and methods.

## Testing and Coverage
Both variants are covered by automated `unittest` suites (`testVector.py` and `testPolynomial.py`). The tests verify arithmetic operations, validation errors, and edge cases. A `.coveragerc` file is used to omit the CLI files (`main.py`), ensuring the automated CI/CD pipeline maintains a coverage of **over 90%** for the core domain logic.

# Lab Assignment #2: Pharmaceutical Distribution Company

## Domain Description
The "Pharmaceutical Distribution Company" is a large-scale object-oriented system designed to manage the end-to-end lifecycle of medicine distribution. The system handles the complexities of pharmaceutical logistics, including inventory tracking, batch expiration management, cold-chain compliance, supplier contracts, client orders, payment processing, and quality control.

## Class Descriptions and Statistics
The system is built using **50 distinct classes** (structured across separate files in `src/models/`). Every class contains meaningful business logic and proper encapsulation.

### Core Entities
- **Manufacturer**: Manages medicine production.
  - *Fields*: `name`, `country`, `license_number`, `medicines`
  - *Methods*: `add_medicine()`
- **Medicine**: The central product.
  - *Fields*: `name`, `dosage`, `form`, `requires_prescription`, `price`, `batches`
  - *Methods*: `set_price()`, `attach_batch()`, `calculate_available_stock()`
- **Batch**: Tracks specific lots of medicine.
  - *Fields*: `batch_number`, `medicine`, `quantity`, `expiry_date`, `is_expired`
  - *Methods*: `mark_expired()`, `deduct_quantity()`
- **Warehouse** & **ColdStorageZone**: Manage physical storage and temperature compliance.
  - *Methods*: `add_stock()`, `remove_stock()`, `monitor_temperature()`

### Client & Personnel
- **Client**, **Pharmacy**, **Hospital**: Manage entities that place orders.
- **Doctor**, **Pharmacist**: Handle prescriptions and dispensing.
- **Employee**, **SalesManager**, **LogisticsManager**, **Driver**: Manage staff operations and payroll.

### Transactions & Orders
- **Order**, **OrderLine**: The core purchasing mechanism.
- **Invoice**, **Payment**: Handle financial transactions and payment status.
- **Prescription**: Validates whether a medicine can be dispensed.
- **Discount**, **PriceList**, **ReturnRequest**, **RefundService**: Handle pricing and financial adjustments.

### Logistics & Quality
- **Vehicle**, **Route**, **Shipment**: Handle the physical delivery of medicines.
- **Recall**, **QualityControl**, **AuditRecord**, **TemperatureLog**: Ensure compliance and safety.
- **Barcode**, **SerialNumber**, **BatchTracker**: Track individual medicine units.

### Services & Analytics
- **InventoryAnalyzer**, **DemandForecaster**, **ReorderPlanner**: Predict stock needs and automate reordering.
- **ReportGenerator**, **Analytics**: Generate business intelligence.
- **NotificationService**, **PaymentGateway**: Handle external integrations.

## Exceptions (12 Custom Classes)
The system uses a robust error-handling architecture with a base exception (`PharmaException`) and 12 specific exceptions:

1. `InsufficientStockException`: Raised when an order exceeds available stock.
2. `InvalidMedicineDataException`: Raised on empty names or negative prices.
3. `ExpiredBatchException`: Raised when dispensing expired medicine.
4. `PrescriptionRequiredException`: Raised when a restricted medicine is sold without a valid prescription.
5. `OrderNotFoundException`: Raised when an invalid order ID is queried.
6. `InvalidOrderStateException`: Raised when modifying an already submitted order.
7. `SupplierNotApprovedException`: Raised when ordering from an unapproved supplier.
8. `ColdChainViolationException`: Raised when storage temperature is out of safe bounds.
9. `InvalidClientDataException`: Raised when registering a client with invalid data.
10. `DuplicateMedicineException`: Raised when adding the same medicine twice.
11. `PaymentFailedException`: Raised when a payment transaction fails or is insufficient.
12. `WarehouseCapacityException`: Raised when a warehouse exceeds its physical capacity.

## CLI Interface
The system includes a fully functional Command-Line Interface (`src/main.py`) that demonstrates the domain's logic:
1. **View Inventory**: Displays all medicines, current stock, and prices.
2. **Place Order**: Allows the user to input a medicine name and quantity, processes the order, and deducts stock.
3. **Add New Medicine**: Dynamically adds new medicines to the inventory.

## Testing and Coverage
The project uses `unittest` for automated testing. The test suite (`tests/test_domain.py`) verifies the core logic of stock deduction, order submission, and exception handling. A `.coveragerc` file is used to isolate core business logic, ensuring the CI/CD pipeline maintains a coverage of **over 90%**.
