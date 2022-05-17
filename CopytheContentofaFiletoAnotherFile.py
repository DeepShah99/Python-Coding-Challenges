with open("/Users/deepshah/Desktop/pythonExercises/14thMay/newfile.txt", "r") as file:
    data = file.readlines()
   

with open("/Users/deepshah/Desktop/pythonExercises/14thMay/newCopiedFile.txt", "w") as writefile:
    for i in data:
        writedata = writefile.write(i)
      
    