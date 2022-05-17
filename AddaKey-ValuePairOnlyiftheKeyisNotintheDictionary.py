dic = {"a": 1, "b" : 2}
newKey = "c"
newVal = 3
if newKey not in dic.keys():
    dic[newKey] = newVal
print(dic)