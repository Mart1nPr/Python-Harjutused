# Text adventure game
# Started: 12/03/2024
# Finished: 

import time
t = 1  # 1-second delay

inventory = ["Hotbar:",[" ", " ", " ", " "],"Abilities:",[" ", " ", " "]]
currency = 0
username = ""
health = 100

def game_start():
    global username
    print("Welcome to Darkmor's Ruler Text Adventure Game!")
    while True:
        time.sleep(t)
        player = input("Enter username: ")
        if len(player) <= 10:
            username = player
            break
        else:
            print()
            print("Username must be 10 characters or fewer. Try again!")
            print()
    the_beginning() # First

def the_beginning():
    time.sleep(t)
    print("Press any key to proceed through the dialog.")
    time.sleep(t)
    
    input(f"Wise Man: Oh, hello {username}! You're finally awake!")
    input("Wise Man: Welcome to the world of TERMINAL, a land of infinite possibilities and unseen dangers.")
    input("Wise Man: TERMINAL is a command-line interface where you can shape reality through words and commands.")
    input("Wise Man: But alas, not all is well. The land is plagued by... *errors*.")
    input("Wise Man: Yes, errors—glitches in the system—have taken over our once peaceful land.")
    input("Wise Man: We sought to stop them, combining my ancient magic with powerful scripts.")
    input("Wise Man: Yet, the errors kept coming, relentless and multiplying...")
    input("Wise Man: Like shadows, they spread, corrupting everything they touch.")
    input(f"Wise Man: But you, {username}, may be the one to restore balance.")
    input("Wise Man: The code calls to you. The system whispers your name...")
    input("Wise Man: Will you rise, face the errors, and save TERMINAL?")
    input("Wise Man: We cannot waste time. The errors grow stronger by the moment!")
    print()
    print("Your journey begins now...")
    print()

def first_quest():
    pass

game_start() # Starts game