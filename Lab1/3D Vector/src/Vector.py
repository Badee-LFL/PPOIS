import math
from numbers import Real
from typing import Self

VECTOR_DIMENSION = 3
DEFAULT_COORDINATE_VALUE = 0.0
COMPARISON_PRECISION_TOLERANCE = 1e-9
ZERO_VECTOR_LENGTH = 0.0


class Vector3D:

    def __init__(
        self,
        x: Real = DEFAULT_COORDINATE_VALUE,
        y: Real = DEFAULT_COORDINATE_VALUE,
        z: Real = DEFAULT_COORDINATE_VALUE,
    ) -> None:
        self.__x = self.__validate_coordinate(x)
        self.__y = self.__validate_coordinate(y)
        self.__z = self.__validate_coordinate(z)

    @staticmethod
    def __validate_coordinate(value: Real) -> float:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("Coordinates must be real numbers.")

        coordinate = float(value)
        if not math.isfinite(coordinate):
            raise ValueError("Coordinates must be finite.")

        return coordinate

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def z(self) -> float:
        return self.__z

    @property
    def coordinates(self) -> tuple[float, float, float]:
        return (self.__x, self.__y, self.__z)

    def length(self) -> float:
        return math.sqrt(
            self.__x**2 + self.__y**2 + self.__z**2
        )

    def dot(self, other: Self) -> float:
        self.__check_vector(other)
        return sum(
            a * b for a, b in zip(self.coordinates, other.coordinates)
        )

    def cross(self, other: Self) -> Self:
        self.__check_vector(other)

        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates

        return type(self)(
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2,
        )

    def cosine_with(self, other: Self) -> float:
        self.__check_vector(other)

        denominator = self.length() * other.length()
        if denominator == ZERO_VECTOR_LENGTH:
            raise ValueError("Cosine is undefined for a zero vector.")

        return self.dot(other) / denominator

    @staticmethod
    def __check_vector(other: object) -> None:
        if not isinstance(other, Vector3D):
            raise TypeError("Operand must be a Vector3D.")

    def __add__(self, other: object) -> Self:
        self.__check_vector(other)
        return type(self)(
            self.__x + other.x,
            self.__y + other.y,
            self.__z + other.z,
        )

    def __sub__(self, other: object) -> Self:
        self.__check_vector(other)
        return type(self)(
            self.__x - other.x,
            self.__y - other.y,
            self.__z - other.z,
        )

    def __mul__(self, other: object) -> Self | float:
        if isinstance(other, Vector3D):
            return self.cross(other)

        if isinstance(other, bool) or not isinstance(other, Real):
            return NotImplemented

        scalar = self.__validate_coordinate(other)
        return type(self)(
            self.__x * scalar,
            self.__y * scalar,
            self.__z * scalar,
        )

    def __rmul__(self, scalar: Real) -> Self:
        result = self.__mul__(scalar)
        if result is NotImplemented:
            return NotImplemented
        return result

    def __truediv__(self, scalar: Real) -> Self:
        if isinstance(scalar, bool) or not isinstance(scalar, Real):
            raise TypeError("Divisor must be a real number.")

        divisor = self.__validate_coordinate(scalar)
        if divisor == ZERO_VECTOR_LENGTH:
            raise ZeroDivisionError("Cannot divide a vector by zero.")

        return type(self)(
            self.__x / divisor,
            self.__y / divisor,
            self.__z / divisor,
        )

    def __neg__(self) -> Self:
        return type(self)(-self.__x, -self.__y, -self.__z)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector3D):
            return NotImplemented

        return all(
            math.isclose(
                a,
                b,
                rel_tol=COMPARISON_PRECISION_TOLERANCE,
                abs_tol=COMPARISON_PRECISION_TOLERANCE,
            )
            for a, b in zip(self.coordinates, other.coordinates)
        )

    def __lt__(self, other: object) -> bool:
        self.__check_vector(other)
        return self.length() < other.length()

    def __le__(self, other: object) -> bool:
        self.__check_vector(other)
        return self.length() <= other.length()

    def __gt__(self, other: object) -> bool:
        self.__check_vector(other)
        return self.length() > other.length()

    def __ge__(self, other: object) -> bool:
        self.__check_vector(other)
        return self.length() >= other.length()

    def __str__(self) -> str:
        return f"({self.__x:g}, {self.__y:g}, {self.__z:g})"

    def __repr__(self) -> str:
        return (
            f"Vector3D({self.__x!r}, "
            f"{self.__y!r}, {self.__z!r})"
        )

    @classmethod
    def from_string(cls, text: str) -> Self:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        cleaned = text.strip()
        if cleaned.startswith("(") and cleaned.endswith(")"):
            cleaned = cleaned[1:-1]

        parts = cleaned.split(",")
        if len(parts) != VECTOR_DIMENSION:
            raise ValueError("A vector must have exactly three coordinates.")

        try:
            coordinates = [float(part.strip()) for part in parts]
        except ValueError as error:
            raise ValueError("Coordinates must be numeric.") from error

        return cls(*coordinates)


