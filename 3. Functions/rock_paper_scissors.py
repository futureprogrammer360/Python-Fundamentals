import random


def get_player_choice():
    print("\nEnter 'rock', 'paper', or 'scissors'. Enter 'q' to quit.")
    player_choice = input("Player: ")
    return player_choice


def get_computer_choice():
    num = random.randint(1, 3)  # 1, 2, 3
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    else:
        return "scissors"


def evaluate(player_choice, computer_choice):
    if player_choice == "rock":
        if computer_choice == "rock":
            return "tied."
        elif computer_choice == "paper":
            return "lost."
        else:
            return "won."
    elif player_choice == "paper":
        if computer_choice == "rock":
            return "won."
        elif computer_choice == "paper":
            return "tied."
        else:
            return "lost."
    else:
        if computer_choice == "rock":
            return "lost."
        elif computer_choice == "paper":
            return "won."
        else:
            return "tied."


def main():
    global playing
    player_choice = get_player_choice()
    if player_choice == "q":
        playing = False
        return
    computer_choice = get_computer_choice()
    print("Computer: " + computer_choice)
    print("You " + evaluate(player_choice, computer_choice))


playing = True
while playing:
    main()
