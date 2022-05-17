h = int(input("please enter the height in cm: "))
w = int(input("please enter the weight in kg: "))
BMI = w/((h/100)**2)
BMI = round(BMI, 1)
print("BMI: " + str(BMI))
if BMI < 18.5:
    print("Underweight")
elif 18.5 < BMI < 24.9:
    print("Normal")
elif 25 < BMI < 29.9:
    print("Overweight")
else:
    print("Obesity")
