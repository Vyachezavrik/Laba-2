
from math import sqrt
print("Поиск полщади треугольника по формуле Герона")
print("Введите стороны треугольника:")
a = float(input("Сторна а = "))
b = float(input("Сторна b = "))
c = float(input("Сторна c = "))
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print("S треугольника =","%.2f" % s)