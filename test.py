from ecc import FieldElement, Point

prime = 223
a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x = FieldElement(num=47, prime=prime)
y = FieldElement(num=71, prime=prime)
p = Point(x, y, a, b)

for s in range(1, 21):
    result = s*p
    print('{}*(47,71)=({},{})'.format(s, result.x.num, result.y.num))


# prime = 223
# a = FieldElement(num=0, prime=prime)
# b = FieldElement(num=7, prime=prime)
# x1 = FieldElement(num=192, prime=prime)
# y1 = FieldElement(num=105, prime=prime)
# x2 = FieldElement(num=17, prime=prime)
# y2 = FieldElement(num=56, prime=prime)
# p1 = Point(x1, y1, a, b)
# p2 = Point(x2, y2, a, b)
# print(p1+p2)

# # p1 = Point(2, 4, 5, 7)
# p2 = Point(-1, -1, 5, 7)
# p3 = Point(18, 77, 5, 7)

# a = FieldElement(7, 13)
# b = FieldElement(12, 13)
# print(a, b, a is b)
# print(a, a, a is a)
# print(a, b, a != b)
# print(a, a, a != a)
# c = FieldElement(6, 13)
# print(a, b, c, a + b == c)

# aa = FieldElement(3, 13)
# bb = FieldElement(12, 13)
# cc = FieldElement(10, 13)

# print(aa, bb, cc, aa*bb == cc)

# dd = FieldElement(1, 13)

# print(aa, dd, aa*dd == aa)

# print(aa, dd, aa**3 == dd)
# print(aa, dd, aa**-3 == dd)
