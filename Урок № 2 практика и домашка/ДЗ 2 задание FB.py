a = int(input("Введите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
for i in list(range(1, c + 1)):
    if (i % a == 0) and not(i % b == 0):
        print("F", end = " ")
    elif(i % b == 0) and not(i % a == 0):
        print("B", end = " ")
    elif(i % a == 0) and (i % b == 0):
        print("FB", end = " ")
    else:
        print(i, end = " ")
