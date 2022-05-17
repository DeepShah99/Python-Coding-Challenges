list = [1, 2, 3, 4]
if len(list) == 0:
    print("Empty List")
else: 
    for i,value in enumerate(list):
      print(str(value) + " " + str(i))