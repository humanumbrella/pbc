from ecc import FieldElement, Point

# p1 = Point(2, 4, 5, 7)
p2 = Point(-1, -1, 5, 7)
p3 = Point(18, 77, 5, 7)

a = FieldElement(7, 13)
b = FieldElement(12, 13)
print(a, b, a is b)
print(a, a, a is a)
print(a, b, a != b)
print(a, a, a != a)
c = FieldElement(6, 13)
print(a, b, c, a + b == c)

aa = FieldElement(3, 13)
bb = FieldElement(12, 13)
cc = FieldElement(10, 13)

print(aa, bb, cc, aa*bb == cc)

dd = FieldElement(1, 13)

print(aa, dd, aa*dd == aa)

print(aa, dd, aa**3 == dd)
print(aa, dd, aa**-3 == dd)
