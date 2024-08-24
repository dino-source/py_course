import random

msg = "Do you want rock, paper or scissors? (type 'quit' to quit)\n"
user_choice = input(msg)

while user_choice != "quit":
    if user_choice == "quit":
        break

    computer_choice = random.choice(["scissors", "rock", "paper"])

    if computer_choice == user_choice:
        print("TIE")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("WIN")
    elif user_choice == "paper" and computer_choice == "rock":
        print("WIN")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("WIN")
    else:
        print("FAIL")
    print("because computer had", computer_choice, "\n")
    user_choice = input(msg)
