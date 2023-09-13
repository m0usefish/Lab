
a = int(input("Введіть а (від 1 до 100): "))
b = int(input("Введіть b (від 1 до 100): "))
while (a < 1 or b > 100):
    a = int(input("Введіть а (від 1 до 100): "))
    b = int(input("Введіть b (від 1 до 100): "))

if a < b:
    res = (a**3 - 5)/b
elif a == b:
    res = -4
else:
    res = (a**4 + b)/a
print( "Результат виразу:",res)