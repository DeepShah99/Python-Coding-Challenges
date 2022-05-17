#dic = {"a": 2, "b" : 2, "c" : 3}
dic = {}
if dic == {}:
    print("Empty")
else:
    bool = True
    x = list(dic.values())[0]
    for i in dic.values():
        if i != x:
            bool = False
            break
    print(bool)