from random import randint


print("Please enter rock, paper, scissor")
choice = input()
choice = choice.lower()
print(choice)
options = ["rock", "paper", "scissor"]
x = options[randint(0,2)]
"""if x == 1:
    x = "rock"
elif x == 2:
    x = "paper"
else:
    x = "scissor"""
print(x)
if choice == x:
    print("It's a tie")
elif choice == "rock" and x == "paper":
    print("you loose, your opponent chose paper")
elif choice == "rock" and x == "scissor":
    print("you win, your opponent chose scissor")
elif choice == "paper" and x == "scissor":
    print("you loose, your opponent chose scissor")
elif choice == "paper" and x == "rock":
    print("you win, your opponent chose rock")
elif choice == "scissor" and x == "paper":
    print("you win, your opponent chose paper")
elif choice == "scissor" and x == "rock":
    print("you loose, your opponent chose rock")
