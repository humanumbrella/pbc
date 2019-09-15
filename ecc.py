# We're creating a field element so we can define ECC math
# this is straight out of the Programming Bitcoin book


class Point:
    def __init__(self, x, y, a, b):
        # y^2 = x^3 + ax + b
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError('({},{}) is not on the curve.'.format(x, y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b


class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, o):
        if o is None:
            return False
        return self.num == o.num and self.prime == o.prime

    def __neq__(self, o):
        return not(self == o)  # This would mean self.num != o.num and self.prime != o.prime

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

    def __floordiv__(self, o):
        if self.prime != o.prime:
            error = 'Cannot divide two numbers in different prime fields.'
            raise TypeError(error)
        pass

    def __pow__(self, exponent):
        # Exponent is just a regular number not a FieldElement.
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
