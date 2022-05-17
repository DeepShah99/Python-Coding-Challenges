l = [1,2,3,4,5]
with open("14thMay/file.txt", "w") as file:
    for i in l:
        i = str(i)
        file.write(i + "\n")