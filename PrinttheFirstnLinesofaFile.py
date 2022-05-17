from email.headerregistry import SingleAddressHeader


num = int(input("Enter a number: "))
if (num > 4):
    print("Please enter a valid number\n")
else:
    with open("10thMay/basic_file.txt") as file:
        random = file.readlines()
        for i in range(num):
            print(random[i].strip())
            





        
  