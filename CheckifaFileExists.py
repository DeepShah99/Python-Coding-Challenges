from genericpath import isfile


file_path = "/Users/deepshah/Desktop/pythonExercises/14thMay/file.txt"
file_exists = isfile(file_path)
if file_path:
    print("the file exists")
else:
    print("the file doesn't exist")