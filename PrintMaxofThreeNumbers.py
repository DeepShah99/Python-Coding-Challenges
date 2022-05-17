a = 7
b = 7 
c = 7
maxi = a
if a > b:
    maxi = a
else:
    maxi = b
if c > maxi:
    maxi = c
print(maxi)

print(max(a,b,c))