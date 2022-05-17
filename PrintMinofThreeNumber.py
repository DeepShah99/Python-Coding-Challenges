a = 7
b = 1 
c = 2
mini = a
if a < b:
    mini = a
else:
    mini = b
if c < mini:
    mini = c
print(mini)
 
print(min(a,b,c))