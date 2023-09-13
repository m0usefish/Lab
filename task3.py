n = 0
while n < 2 or n > 9:
    n = int(input("Введіть цифру від 2 до 9: "))

for i in range(1, n + 1):
    num = 1
    count = 0
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end = " ")
            count +=1
        else:
            print(num+count, end = " ")
            num += 1
    print("")




