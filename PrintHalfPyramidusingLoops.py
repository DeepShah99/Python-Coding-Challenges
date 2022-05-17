n = int(input("Enter a number: "))
space = n - 1
for i in range(1, n+1):
    for j in range(1, space+1):
        print(" ", end =" ")
    space = space - 1
    for k in range(1, i+1):
        print("*", end =" ")
    print("\n")