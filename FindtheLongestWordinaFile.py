max = 0
max_word = ""
with open("10thMay/words.txt") as file:
    words = file.readlines()
    print(words)
    for i in words:
        current = len(i)
        if current > max:
            max = current
            max_word = i


print(max_word.strip())
        