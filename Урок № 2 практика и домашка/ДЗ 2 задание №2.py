weaght = int(input("Введите целое число в килограммах: "))
heaght = float(input("Введите рост в метрах: "))
bmi = weaght / (heaght ** 2)
if bmi < 25:
    print("У тебя идеальный вес")
elif (bmi >= 25) and (bmi < 30):
    print("Вставай и иди тренироваться в спортзал")
else:
    print("Чувак если не начнешь тренироваться, то хана")
