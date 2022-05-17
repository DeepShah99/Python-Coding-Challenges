h = 7
space = h - 4 
star = 1
midheight = h/2 - 0.5 + 1
midheight = int(midheight)
for i in range(1, midheight + 1):
    for j in range(0, space):
        print(" ", end = "")
    for k in range(0, star):
        print("*", end = "")
    print(" ")
    space -= 1
    star += 2
h2 = h - midheight
space = 1
star = h - 2
for i in range(1, h2+1):
    for j in range(1, space + 1):
        print(" ", end = "")
    for k in range(0, star):
        print("*", end = "")
    print(" ")
    space += 1
    star -= 2


