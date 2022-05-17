from itertools import count


#l = [1, 1, 2, 3, 3]
l = ["a", "b", "A", "c"]
dic = {}
for i in l:
    if i not in dic:
        dic[i] = l.count(i)
print(dic)