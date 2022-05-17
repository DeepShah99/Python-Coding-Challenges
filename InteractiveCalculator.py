print("=== Welcome to your Interactive Python Calculator ===")
print("Please enter the first value: ")
x = int(input())
print("Please enter the second value: ")
y = int(input())
print("""Great! Now enter the operation
These are the available options:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
5 - Integer Division
6 - Modulo""")
print("--> Enter the corresponding integer: ")
z = int(input())
print(x,y,z)
if z == 1:
    result = x + y
    print("The result of " + str(x) + "+" + str(y) + "is: " + str(result))
