"""Polynomial represented by coefficients in ascending power order."""
import math
from numbers import Real
from typing import Self

DEFAULT_COEFFICIENT = 0.0
ZERO_POLYNOMIAL_DEGREE = 0
DIVISION_TOLERANCE = 1e-10


class Polynomial:

    def __init__(self, *coefficients: Real) -> None:
        if not coefficients:
            coefficients = (DEFAULT_COEFFICIENT,)

        validated = []
        for value in coefficients:
            if not self.is_valid_coefficient(value):
                self.__raise_invalid_coefficient(value)
            validated.append(float(value))

        while len(validated) > 1 and validated[-1] == DEFAULT_COEFFICIENT:
            validated.pop()

        self.__coefficients = tuple(validated)

    def is_valid_coefficient(self, value: object) -> bool:
        return (
            isinstance(value, Real)
            and not isinstance(value, bool)
            and math.isfinite(value)
        )

    def __raise_invalid_coefficient(self, value: object) -> None:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Polynomial coefficients must be real numbers.")
        raise ValueError("Polynomial coefficients must be finite.")

    def is_valid_polynomial(self, other: object) -> bool:
        return isinstance(other, Polynomial)

    def __require_polynomial(self, other: object) -> None:
        if not self.is_valid_polynomial(other):
            raise TypeError("Operand must be a Polynomial.")

    @property
    def coefficients(self) -> tuple[float, ...]:
        return self.__coefficients

    def copy(self) -> Self:
        return type(self)(*self.__coefficients)

    @property
    def degree(self) -> int:
        if self.is_zero():
            return ZERO_POLYNOMIAL_DEGREE
        return len(self.__coefficients) - 1

    def is_zero(self) -> bool:
        return all(value == DEFAULT_COEFFICIENT for value in self.__coefficients)

    def __getitem__(self, power: int) -> float:
        if not isinstance(power, int) or isinstance(power, bool):
            raise TypeError("Power must be an integer.")
        if power < 0:
            raise IndexError("Power cannot be negative.")
        if power >= len(self.__coefficients):
            return DEFAULT_COEFFICIENT
        return self.__coefficients[power]

    def evaluate(self, x: Real) -> float:
        if not self.is_valid_coefficient(x):
            self.__raise_invalid_coefficient(x)
        value = float(x)
        result = DEFAULT_COEFFICIENT
        for coefficient in reversed(self.__coefficients):
            result = result * value + coefficient
        return result

    def __add__(self, other: object) -> Self:
        if not self.is_valid_polynomial(other):
            return NotImplemented
        size = max(len(self.__coefficients), len(other.__coefficients))
        return type(self)(*(self[index] + other[index] for index in range(size)))

    def __sub__(self, other: object) -> Self:
        if not self.is_valid_polynomial(other):
            return NotImplemented
        size = max(len(self.__coefficients), len(other.__coefficients))
        return type(self)(*(self[index] - other[index] for index in range(size)))

    def __mul__(self, other: object) -> Self:
        if isinstance(other, Real) and not isinstance(other, bool):
            if not self.is_valid_coefficient(other):
                self.__raise_invalid_coefficient(other)
            scalar = float(other)
            return type(self)(*(value * scalar for value in self.__coefficients))

        if not self.is_valid_polynomial(other):
            return NotImplemented

        result_size = len(self.__coefficients) + len(other.__coefficients) - 1
        result = [DEFAULT_COEFFICIENT] * result_size
        for left_power, left_value in enumerate(self.__coefficients):
            for right_power, right_value in enumerate(other.__coefficients):
                result[left_power + right_power] += left_value * right_value
        return type(self)(*result)

    def __rmul__(self, scalar: Real) -> Self:
        return self.__mul__(scalar)

    def __truediv__(self, other: object) -> Self:
        if isinstance(other, Real) and not isinstance(other, bool):
            if not self.is_valid_coefficient(other):     
                self.__raise_invalid_coefficient(other)
            divisor = float(other)
            if divisor == DEFAULT_COEFFICIENT:
                raise ZeroDivisionError("Cannot divide by zero.")
            return type(self)(*(value / divisor for value in self.__coefficients))

        if not self.is_valid_polynomial(other):
            return NotImplemented
        if other.is_zero():
            raise ZeroDivisionError("Cannot divide by the zero polynomial.")
        if len(other.coefficients) == 1:
            return self.__divide_by_constant(other.coefficients[0])
        return self.__divide_by_polynomial(other)

    def __divide_by_constant(self, divisor: float) -> Self:
        if divisor == DEFAULT_COEFFICIENT:
            raise ZeroDivisionError("Cannot divide by zero.")
        return type(self)(*(value / divisor for value in self.__coefficients))

    def __divide_by_polynomial(self, divisor: Self) -> Self:
        remainder = list(self.__coefficients)
        divisor_coefficients = divisor.coefficients
        quotient_size = max(1, len(remainder) - len(divisor_coefficients) + 1)
        quotient = [DEFAULT_COEFFICIENT] * quotient_size
        self.__trim_remainder(remainder)

        while (
            len(remainder) >= len(divisor_coefficients)
            and not (len(remainder) == 1 and remainder[0] == 0.0)
        ):
            power = len(remainder) - len(divisor_coefficients)
            factor = remainder[-1] / divisor_coefficients[-1]
            quotient[power] += factor
            for index, coefficient in enumerate(divisor_coefficients):
                remainder[power + index] -= factor * coefficient
            self.__trim_remainder(remainder)

        if any(abs(value) >= DIVISION_TOLERANCE for value in remainder):
            raise ValueError("Polynomial division has a nonzero remainder.")
        return type(self)(*quotient)

    def __trim_remainder(self, remainder: list[float]) -> None:
        while (
            len(remainder) > 1
            and abs(remainder[-1]) < DIVISION_TOLERANCE
        ):
            remainder.pop()
        if len(remainder) == 1 and abs(remainder[0]) < DIVISION_TOLERANCE:  
            remainder[0] = DEFAULT_COEFFICIENT  


    def __eq__(self, other: object) -> bool:
        if not self.is_valid_polynomial(other):
            return NotImplemented
        return self.__coefficients == other.__coefficients

    def __neg__(self) -> Self:
        return type(self)(*(-value for value in self.__coefficients))

    def __str__(self) -> str:
        return f"[{', '.join(f'{value:g}' for value in self.__coefficients)}]"

    def __repr__(self) -> str:
        values = ", ".join(repr(value) for value in self.__coefficients)
        return f"Polynomial({values})"

    @classmethod
    def from_string(cls, text: str) -> Self:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        cleaned = text.strip()
        if cleaned.startswith("[") and cleaned.endswith("]"):
            cleaned = cleaned[1:-1].strip()
        if not cleaned:
            return cls(DEFAULT_COEFFICIENT)
        try:
            coefficients = [float(part.strip()) for part in cleaned.split(",")]
        except ValueError as error:
            raise ValueError("Coefficients must be numeric.") from error
        return cls(*coefficients)
