#sRaw = "The quick brown fox jumps over the lazy dog"
"""sRaw = "bcdefghijklmnopqrstuvwxyza"

s = sRaw.lower()
alph = "abcdefghijklmnopqrstuvwxyz"
bool = True
for i in alph:
    for j in s:
        if i == j:
            bool = True
            break
        else:
            bool = False
    if bool == False:
        break
print(bool)"""

import string
sRaw = "The quick brown fox jumps over the lazy dog"
s = sRaw.lower()
s = s.replace(" ", "")
set_s = set(s)
print(s)
print(set_s)
print(set_s == set(string.ascii_lowercase))