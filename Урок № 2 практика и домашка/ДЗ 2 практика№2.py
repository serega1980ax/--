number = int(input("Plese enter a number"))
if (number %2) and not(number %3) and not(number %5):
    print("This is the number we are searching for")
else:
    print("The number is wrong")