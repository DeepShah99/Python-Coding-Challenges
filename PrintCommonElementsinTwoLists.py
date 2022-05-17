A = [1, 2, 3]
B = [4, 5, 6]
C = []
for i in A:
    if i in B:
        C.append(i)

print(C)