#option 1
basicfile = open("10thMay/basic_file.txt", "r")
print(basicfile.readlines())
basicfile.close()

#option 2
emptylist = []
with open("10thMay/basic_file.txt", "r") as random:
    #print(random.readlines())
    emptylist = random.readlines()
    print(emptylist)

#option 3
basicfile = "10thMay/basic_file.txt"
list = []
with open(basicfile) as file:
    for line in file:
        list.append(line)
print(list)

"""Text file is 
Line 1
Line 2
Line 3
Line 4
"""
