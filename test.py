from ecc import FieldElement

a = FieldElement(7,13)
b = FieldElement(12,13)
print(a == b)
print(a == a)
print(a != b)
print(a != a)
c = FieldElement(6,13)
print(a+b == c)

aa = FieldElement(3,13)
bb = FieldElement(12,13)
cc = FieldElement(10,13)

print(aa*bb==cc)

dd = FieldElement(1,13)

print(aa*dd == aa)

print(aa**3 == dd)
print(aa**-3 == dd)
