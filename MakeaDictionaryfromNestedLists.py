my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]
my_dict = {}

"""for i in my_list:
    for j in i:
        if type(j) == str:
            key = j
        if type(j) == int:
            value = j
        
    my_dict[key] = value
       
print(my_dict)"""

for nestedList in my_list:
    key = nestedList[0]
    value = nestedList[1]
    my_dict[key] = value

print(my_dict)
