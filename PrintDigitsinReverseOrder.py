num = 123
num = str(num)
for i in range(len(num)-1,-1,-1):
    print(num[i], end="")

print("\n"+ num[::-1])