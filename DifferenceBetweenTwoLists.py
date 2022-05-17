A = [1, 3, 4, 2]
B = [1, 3, 4]
C = []
for i in A:
    if i not in B:
        C.append(i)
print(C)
