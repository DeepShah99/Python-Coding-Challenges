s = "deepo"

def vowel(s, count):
    if len(s) == 0:
        return count
    else:
        if s[0] in ("a", "e", "i", "o", "u"):
            count += 1
        return vowel(s[1::], count)

print(vowel(s, 0))