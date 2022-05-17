from cmath import sqrt


a = 1
b = 2
c = 1
disc = b*b - 4*a*c 
if disc > 0:
    x1 = (-b - sqrt(disc))/(2*a)
    x2 = ((sqrt(disc) - b))/(2*a)
    print(x1,x2)
elif disc < 0:
    print("Complex roots")
else:
    x1 = (-b - sqrt(disc))/(2*a)
    print(x1)
