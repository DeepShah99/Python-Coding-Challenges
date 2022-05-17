n = int(input("Enter a number: "))
count = 1
for row in range(1, n + 1):
    for i in range(0, row):
        print(count, end = " ")
        count += 1
    print("")


