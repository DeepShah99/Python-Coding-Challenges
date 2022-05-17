#l = [2,4,[1,2,3], [4,5,6],[1,8,9]]
l = ["a", ["b", "c", 2], "d"]

newl = []
for i in range(0, len(l)):
    if isinstance(l[i], list) == True:
        for j in l[i]:
            newl.append(j)
    else:
        newl.append(l[i])



print(newl)