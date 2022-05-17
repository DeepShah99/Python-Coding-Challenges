count = 0
with open("/Users/deepshah/Desktop/pythonExercises/14thMay/newfile.txt", "r") as file:
    filedata = file.readlines()
    print(filedata)
    for i in filedata:
        i = i.replace(" ", "")
        i = i.strip()
        print(i)
        count = count + len(i)
print(count)

"""
"Computer Science is no more about computers than astronomy is about telescopes." by Edsger W. Dijkstra
"The computer was born to solve problems that did not exist before." by Bill Gates
"Quiet people have the loudest minds." by Stephen Hawking
"Tell me and I forget. Teach me and I remember. Involve me and I learn." by Benjamin Franklin
"Intelligence is the ability to adapt to change." by Stephen Hawking
"""