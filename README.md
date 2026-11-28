# ppoiss_labs

Labs for the *Design of Intelligent Systems Software* course.

## Structure

- `lab1/3D_Vector/` — Lab 1: 3D Vector (OOP fundamentals)
- `lab1/Polynomial/` — Lab 1: Single-Variable Polynomial (OOP fundamentals)
- `lab2/Pharma_Distribution/` — Lab 2: Pharmaceutical Distribution Company (Large-scale OOP)
- `lab3/Online_Learning/` — Lab 3: Online Learning Platform (Large-scale OOP)

## Lab 1: 3D Vector & Polynomial

Python implementations of a 3D Vector and a single-variable polynomial.

- **Domain models:** `lab1/3D_Vector/src/Vector.py` and `lab1/Polynomial/src/Polynomial.py`
- **Interactive CLIs:** `lab1/3D_Vector/src/main.py` and `lab1/Polynomial/src/main.py`
- **Tests:** `lab1/3D_Vector/tests/` and `lab1/Polynomial/tests/` (>90% coverage)
- **Docs:** generated with `pdoc` (see `docs/` folders in each variant)

## Lab 2: Pharmaceutical Distribution Company

A large-scale OOP system managing the lifecycle of medicine distribution.

- **Domain model:** `lab2/Pharma_Distribution/src/models/` (50 classes, 12 exceptions)
- **Interactive CLI:** `lab2/Pharma_Distribution/src/main.py`
- **Tests:** `lab2/Pharma_Distribution/tests/` (>90% coverage)
- **Architecture:** 1 file per class, utilizing `.coveragerc` for strict coverage testing.

## Lab 3: Online Learning Platform

A large-scale OOP system managing educational content and enrollments.

- **Domain model:** `lab3/Online_Learning/src/models/` (51 classes, 12 exceptions)
- **Interactive CLI:** `lab3/Online_Learning/src/main.py`
- **Tests:** `lab3/Online_Learning/tests/` (>90% coverage)
- **Architecture:** 1 file per class, utilizing `.coveragerc` for strict coverage testing.

## Setup
To run the project locally, you can set up a virtual environment:

```bash
python -m venv .venv

# On Linux/macOS:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

pip install coverage
