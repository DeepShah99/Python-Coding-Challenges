list = ["a", "b" ,"c", "d"]
 #option 1
factor = 2
result = [i * factor for i in list]
print(result)

 #option 2
for i in range(0, len(list)):
    list[i] *= factor
print(list)

 #option 3
myList = []
for i in range(0, len(list)):
    x = list[i] * factor
    myList.append(x)
print(myList)

 #option 4
for count,listValues in enumerate(list):
    list[count] *= factor
print(list)
