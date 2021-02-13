file = open("FizzBazz.txt", "r")
write_file1 = open("FizzBazz1.txt", "w")
num = 0

for line in file:
    num += 1
    if not line:
        break

    y = line.split()
    a = int(y[0])
    b = int(y[1])
    c = int(y[2])
    for i in list(range(1, c + 1)):
        if(i % a == 0) and not (i % b == 0):
            print("F", end=" ", file=write_file1)
        elif (i % b == 0) and not (i % a == 0):
            print("B", end=" ", file=write_file1)
        elif (i % a == 0) and (i % b == 0):
            print("FB", end=" ", file=write_file1)
        else:
            print(i, end=" ", file=write_file1)
    print("\n", end=" ", file=write_file1)
file.close()
write_file1.close()
