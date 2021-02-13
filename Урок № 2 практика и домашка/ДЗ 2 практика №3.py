a = int(input("Введите целое число: "))
print("Результат: ")
for i in range(a - 1, 1, -1):
    if (a%i ==0):
        print(i)