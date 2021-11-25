from random import randint

# Stores wins for the player and computer
player_wins = 0
cpu_wins = 0


def pick_option():
    """
    Provides input for the player to enter their play option and then checks if
    the entered input key is valid and then return the choice of the player
    """
    player_choice = input("Choose Rock, Paper, or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "p"
    else:
        print("Invalid input, try using r = Rock, p = Paper, s = Scissors")
        pick_option()
    return player_choice

pick_option()