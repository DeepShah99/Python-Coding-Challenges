from curses.ascii import isalpha


s = "Score: 36"
s = s.lower()
print(s)
if not s:
    print("empty string")
else:
    for i in s:
        if i in ("a","e","i","o","u"):
            print(i + " is a vowel")
        elif isalpha(i) == False:
            print(i + " is not a letter")
        else:
            print(i + " is a consonent")
