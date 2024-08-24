import random


def roll_dice(number_of_dices):
    result = 0
    while (number_of_dices > 0):
        result += random.randint(1, 6)
        number_of_dices -= 1
    return result


def results(player1, player2):
    if player1["roll"] > player2["roll"]:
        print(player1["name"], "wins!")
    elif player2["roll"] > player1["roll"]:
        print(player2["name"], "wins!")
    else:
        print("You tie!")


def main():
    roll1 = roll_dice(4)
    roll2 = roll_dice(4)
    player1 = {"name": "Ian", "roll": roll1}
    player2 = {"name": "Bob", "roll": roll2}

    print(player1["name"], "rolled", player1["roll"])
    print(player2["name"], "rolled", player2["roll"])
    results(player1, player2)


main()

