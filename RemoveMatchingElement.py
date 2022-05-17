list = [6,7,6,4]
elem_to_remove = 6
printMsg = True
if len(list) == 0:
    print("Empty List")
    printMsg = False
elif list.count(elem_to_remove) == 0:
    print("Not Found")
    printMsg = False
else:
    for i in range(1, list.count(elem_to_remove) + 1):
        list.remove(elem_to_remove)

if printMsg == True:
    print(list)