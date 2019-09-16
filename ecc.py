# We're creating a field element so we can define ECC math
# this is straight out of the Programming Bitcoin book


class Point:
    def __init__(self, x, y, a, b):
        # y^2 = x^3 + ax + b
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + self.a * self.x + self.b:
            raise ValueError('({},{}) is not on the curve.'.format(x, y))

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y
                and self.a == other.a and self.b == other.b)

    def __ne__(self, other):
        return (self.x != other.x or self.y != other.y
                or self.a != other.a or self.b != other.b)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError('({}, {}) is not on the same curve.'.format(self, other))

        if self.x is None:
            return other
        if other.x is None:
            return self

        # if self == other and self.y == 0 * self.x:
        #     return

        if self is other:
            # tangent line to this point.
            # One more special case here if we're at y == 0, should return
            # the point at infinity.
            # if self.y == (0 * self.x):
            #    return self.__class__(None, None, self.a, self.b)
            s = (3 * self.x**2 + self.a) / (2 * self.y)
            x_3 = s**2 - 2 * self.x
            y_3 = s * (self.x - x_3) - self.y
            return self.__class__(x_3, y_3, self.a, self.b)

        # This is point addition via slope and reflection over x-axis
        if self.x is not other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x_3 = s**2 - self.x - other.x
            y_3 = s * (self.x - x_3) - self.y
            return self.__class__(x_3, y_3, self.a, self.b)

        if self.x == other.x and self.y != other.y:  # additive inverse
            return self.__class__(None, None, self.a, self.b)

    def __rmul__(self, scalar_multiple):
        current = self
        result = self.__class__(None, None, self.a, self.b)
        while scalar_multiple:
            if scalar_multiple & 1:
                result += current
            current += current
            scalar_multiple >>= 1
        return result

    # def __rmul__(self, scalar_multiple):
    #     product = self.__class__(None, None, self.a, self.b)
    #     for _ in range(scalar_multiple):
    #         product += self
    #     return product


class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)
            raise ValueError(error)
        self.num = num
        # FIXME -- is prime prime? lol
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, o):
        if o is None:
            return False
        return self.num == o.num and self.prime == o.prime

    def __ne__(self, o):
        return (self.num != o.num or self.prime != o.prime)
        # return self is not o  # This would mean self.num != o.num and self.prime != o.prime

    def __add__(self, o):
        if self.prime != o.prime:
            error = 'Cannot add two numbers in different prime fields.'
            raise TypeError(error)
        num = (self.num + o.num) % self.prime
        # could just return a FieldElement here
        # but this provides a better mechanism for inheritance.
        return self.__class__(num, self.prime)

    def __sub__(self, o):
        if self.prime != o.prime:
            error = 'Cannot subtract two numbers in different prime fields.'
            raise TypeError(error)
        num = (self.num - o.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, o):
        if self.prime != o.prime:
            error = 'Cannot multiply two numbers in different prime fields.'
            raise TypeError(error)
        num = (self.num * o.num) % self.prime
        return self.__class__(num, self.prime)

    def __truediv__(self, o):
        if self.prime != o.prime:
            error = 'Cannot divide two numbers in different prime fields.'
            raise TypeError(error)
        # use Fermat's little theorem: self.num ** (p-1) % p == 1
        # 1/n = pow(n,p-2,p)
        num = self.num * pow(o.num, self.prime-2, self.prime) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        # Exponent is just a regular number not a FieldElement.
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)


class ECCTest():

    def test_on_curve(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)
        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))

        for x_plain, y_plain in valid_points:
            x = FieldElement(x_plain, prime)
            y = FieldElement(y_plain, prime)
            Point(x, y, a, b)

        for x_plain, y_plain in invalid_points:
            x = FieldElement(x_plain, prime)
            y = FieldElement(y_plain, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)
