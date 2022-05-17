h = int(input("Enter the height: "))
b = int(input("Enter the base: "))
a = (h * b)/2
a = round(a, 2)
if h > 0 and b > 0:
    print("the area of triangle is " + str(a))
else:
    print("enter valid values of h and b")

