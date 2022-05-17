#dic = {"a" : 1, "c" : 3,"b" : 2}
dic = {}

"""if dic == {}:
    print(None)
else:
    largest = list(dic.values())[0]
    for i in dic.values():
        if i > largest:
            largest = i
    print(largest)"""

if dic:
    largest = max(set(dic.values()))
    print(largest)
else:
    print(None)
    
