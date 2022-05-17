from email.headerregistry import SingleAddressHeader


num = int(input("Enter a number: "))
if (num > 4):
    print("Please enter a valid number\n".strip())
else:
    with open("10thMay/basic_file.txt") as file:
        random = file.readlines()
        line_length = len(random)
        starting_point = 4 - num 
        for i in range(starting_point, line_length):
            print(random[i].strip())
            