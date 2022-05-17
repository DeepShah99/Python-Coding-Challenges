from itertools import count


dict_words = {}
with open("10thMay/words.txt") as file:
    data = file.readlines()
    for word in data:
        word = word.strip()
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1


print(dict_words)

"""
switch
concert
contradiction
offset
power
concert
concert
offset
"""