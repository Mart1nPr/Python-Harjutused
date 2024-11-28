# Rock, Paper, Scissors
# 11/28/2024

import random

Tools = [
    "Rock",
    "Paper",
    "Scissors"
]

def gameBegin():
    robotGuess = random.choice(Tools)
    if humanGuess.lower() == robotGuess.lower():
        print("It's a tie!")
    elif humanGuess.lower() == "rock" and robotGuess == "paper" or \
        humanGuess.lower() == "paper" and robotGuess == "rock" or \
        humanGuess.lower() == "scissors" and robotGuess == "paper":
        print("You won!")
    else:
        print("You lost... Robot wins!")

humanGuess = input("Choose (Rock/Paper/Scissors): ").lower()
if humanGuess not in ["rock", "paper", "scissors"]:
    print("Invalid input choose (Rock/Paper/Scissors)")
else:
    gameBegin()




