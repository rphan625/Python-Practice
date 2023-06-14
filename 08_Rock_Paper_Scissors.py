""" Exercise 8 
    Rock Paper Scissors
    Make 2 player rock-paper-scissors
"""

gameRunning = True

while gameRunning:
    my_choice = input("Player: Rock, Paper, or Scissor?: ")
    opponent = input("Opponent: Rock, Paper, or Scissor?: ")

    if opponent == "Rock":
        if my_choice == "Rock":
            print("Tie Game!")
        elif my_choice == "Paper":
            print("Player 1 Wins!")
        else:
            print("Player 2 Wins!")
    elif opponent == "Paper":
        if my_choice == "Rock":
            print("Player 2 Wins!")
        elif my_choice == "Paper":
            print("Tie Game!")
        else:
            print("Player 1 Wins!")
    elif opponent == "Scissor":
        if my_choice == "Rock":
            print("Player 1 Wins!")
        elif my_choice == "Paper":
            print("Player 2 Wins!")
        else:
            print("Tie Game!")

    replay = input("Would you like to play again? (y/n): ")

    if replay == "y" or replay == "Y":
        continue
    else:
        gameRunning = False
print("Game Over!")
