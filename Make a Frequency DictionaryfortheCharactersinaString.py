from curses.ascii import isalpha


s = "HelLo, World"
s = s.lower()
my_dict = {}
for i in s:
    if isalpha(i):     
        my_dict[i] = s.count(i)

print(my_dict)

    