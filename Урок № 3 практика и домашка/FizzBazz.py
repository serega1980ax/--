file = open("FizzBazz.txt", "r")
file1 = open("FizzBazz1.txt", "w")
for s in file:
    y = list(map(int, s.split()))
    a = int(y[0])
    b = int(y[1])
    c = int(y[2])
    for i in list(range(1, c + 1)):
        if(i % a == 0) and not (i % b == 0):
            print("F", end=" ")
        elif (i % b == 0) and not (i % a == 0):
            print("B", end=" ")
        elif (i % a == 0) and (i % b == 0):
            print("FB", end=" ")
        else:
            print(i, end=" ")
file.close()
file1.close()
