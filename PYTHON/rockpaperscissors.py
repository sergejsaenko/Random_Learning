import random


def play():
    user = input("Please use 'R' for rock, 'P' for paper and 'S' for scissors: ").lower()
    computer = random.choice(["r", "p", "s"])

    if user=="r":
        print("Player chose: Rock")
    elif user=="p":
        print("Player chose: Paper")
    elif user=="s":
        print("Player chose: Scissors")

    if computer=="r":
        print("Computer chose: Rock")
    elif computer=="p":
        print("Computer chose: Paper")
    elif computer=="s":
        print("Computer chose: Scissors")

    if user == computer:
        return "tie"

    #r>s, s>p, p>r
    if is_win(user, computer):
        return "You won!"
    return "You lost!"


def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

print(play())
