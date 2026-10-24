"""Three-dimensional vector implemented with object-oriented principles."""
import math
from numbers import Real
from typing import Self

VECTOR_DIMENSION = 3
DEFAULT_COORDINATE_VALUE = 0.0
COMPARISON_PRECISION_TOLERANCE = 1e-9
ZERO_VECTOR_LENGTH = 0.0


class Vector3D:
    """Represent a three-dimensional vector with encapsulated coordinates."""

    def __init__(
        self,
        x: Real = DEFAULT_COORDINATE_VALUE,
        y: Real = DEFAULT_COORDINATE_VALUE,
        z: Real = DEFAULT_COORDINATE_VALUE,
    ) -> None:
        self.__x = self.__convert_coordinate(x)
        self.__y = self.__convert_coordinate(y)
        self.__z = self.__convert_coordinate(z)

    def is_valid_coordinate(self, value: object) -> bool:
        """Return True when value is a finite real number (but not bool)."""
        return (
            isinstance(value, Real)
            and not isinstance(value, bool)
            and math.isfinite(value)
        )

    def __convert_coordinate(self, value: object) -> float:
        """Validate and convert a coordinate to float."""
        if not self.is_valid_coordinate(value):
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("Coordinates must be real numbers.")
            raise ValueError("Coordinates must be finite.")
        return float(value)

    def is_valid_vector(self, other: object) -> bool:
        """Return whether other is a Vector3D instance."""
        return isinstance(other, Vector3D)

    def __require_vector(self, other: object) -> None:
        """Raise a clear error when an operation needs another vector."""
        if not self.is_valid_vector(other):
            raise TypeError("Operand must be a Vector3D.")

    @property
    def x(self) -> float:
        """Return the x-coordinate."""
        return self.__x

    @property
    def y(self) -> float:
        """Return the y-coordinate."""
        return self.__y

    @property
    def z(self) -> float:
        """Return the z-coordinate."""
        return self.__z

    @property
    def coordinates(self) -> tuple[float, float, float]:
        """Return all coordinates as an immutable tuple."""
        return (self.__x, self.__y, self.__z)

    def copy(self) -> Self:
        """Return an independent vector with the same coordinates."""
        return type(self)(self.__x, self.__y, self.__z)

    def length(self) -> float:
        """Return the Euclidean length."""
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    def dot(self, other: Self) -> float:
        """Return the dot product with another vector."""
        self.__require_vector(other)
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))

    def cross(self, other: Self) -> Self:
        """Return the cross product with another vector."""
        self.__require_vector(other)
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        return type(self)(
            y1 * z2 - z1 * y2,
            z1 * x2 - x1 * z2,
            x1 * y2 - y1 * x2,
        )

    def cosine_with(self, other: Self) -> float:
        """Return the cosine of the angle between two nonzero vectors."""
        self.__require_vector(other)
        denominator = self.length() * other.length()
        if denominator == ZERO_VECTOR_LENGTH:
            raise ValueError("Cosine is undefined for a zero vector.")
        return self.dot(other) / denominator

    def __add__(self, other: object) -> Self:
        """Add two vectors."""
        self.__require_vector(other)
        return type(self)(
            self.__x + other.x,
            self.__y + other.y,
            self.__z + other.z,
        )

    def __sub__(self, other: object) -> Self:
        """Subtract another vector."""
        self.__require_vector(other)
        return type(self)(
            self.__x - other.x,
            self.__y - other.y,
            self.__z - other.z,
        )

    def __mul__(self, other: object) -> Self:
        """Multiply by a scalar or take the cross product of two vectors."""
        if self.is_valid_vector(other):
            return self.cross(other)
        if isinstance(other, bool) or not isinstance(other, Real):
            return NotImplemented
        scalar = self.__convert_coordinate(other)
        return type(self)(
            self.__x * scalar,
            self.__y * scalar,
            self.__z * scalar,
        )

    def __rmul__(self, scalar: Real) -> Self:
        """Support scalar multiplication with the scalar on the left."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Real) -> Self:
        """Divide by a finite, nonzero real scalar."""
        if isinstance(scalar, bool) or not isinstance(scalar, Real):
            raise TypeError("Divisor must be a real number.")
        divisor = self.__convert_coordinate(scalar)
        if divisor == ZERO_VECTOR_LENGTH:
            raise ZeroDivisionError("Cannot divide a vector by zero.")
        return type(self)(
            self.__x / divisor,
            self.__y / divisor,
            self.__z / divisor,
        )

    def __neg__(self) -> Self:
        """Return a vector with all coordinates negated."""
        return type(self)(-self.__x, -self.__y, -self.__z)

    def __eq__(self, other: object) -> bool:
        """Compare coordinates with a floating-point tolerance."""
        if not self.is_valid_vector(other):
            return NotImplemented
        return all(
            math.isclose(
                first,
                second,
                rel_tol=COMPARISON_PRECISION_TOLERANCE,
                abs_tol=COMPARISON_PRECISION_TOLERANCE,
            )
            for first, second in zip(self.coordinates, other.coordinates)
        )

    def __lt__(self, other: object) -> bool:
        """Compare vectors by length."""
        self.__require_vector(other)
        return self.length() < other.length()

    def __le__(self, other: object) -> bool:
        """Compare vector lengths using less-than-or-equal."""
        self.__require_vector(other)
        return self.length() <= other.length()

    def __gt__(self, other: object) -> bool:
        """Compare vectors by length using greater-than."""
        self.__require_vector(other)
        return self.length() > other.length()

    def __ge__(self, other: object) -> bool:
        """Compare vector lengths using greater-than-or-equal."""
        self.__require_vector(other)
        return self.length() >= other.length()

    def __str__(self) -> str:
        """Return a readable coordinate representation."""
        return f"({self.__x:g}, {self.__y:g}, {self.__z:g})"

    def __repr__(self) -> str:
        """Return a constructor-style representation."""
        return f"Vector3D({self.__x!r}, {self.__y!r}, {self.__z!r})"

    @classmethod
    def from_string(cls, text: str) -> Self:
        """Create a vector from three comma-separated coordinates."""
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
