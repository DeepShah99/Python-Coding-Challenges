s = "ABCD"
i = len(s) - 1
result = ""

while i >= 0:
    result = result + s[i]
    i-=1
    
print(result)

print(s[::-1])


