
print("Введите цифры трехзначного числа:")
a1 = int(input("Количество единиц - "))
a2 = int(input("Количество десятков -  "))
a3 = int(input("Количество сотен - "))
print("Введите цифры двухзначного числа:")
b1 = int(input("Количество едениц - "))
b2 = int(input("Количество десятков - "))

c = (a1 + b1) % 10
d = (a2 + b2 + (a1 + b1))//10
e = (a3 + (a2 + b2 + (a1 + b1)))//10
print("Цыфры числа равные ссуме заданных чисел:", e, d, c)