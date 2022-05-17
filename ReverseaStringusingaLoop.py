s = "Hello"
print(s[::-1])
for i in range(len(s)-1,-1,-1):
    print(s[i], end="")
print("\n")
for i in reversed(s):
    print(i, end="")