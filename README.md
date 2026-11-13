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
