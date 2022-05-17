dic = {"a" : 1, "c" : 3,"b" : 2}
#dic = {}

if dic:
    smallest = min(set(dic.values()))
    print(smallest)
else:
    print(None)
    