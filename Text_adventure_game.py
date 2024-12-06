# Text adventure game
# Started: 12/03/2024
# Finished: 

import time
t = 1  # 1-second delay

inventory = ["Inventory:",[" ", " ", " ", " "]]
currency = 0
username = ""
health = 100

# Enemy health
skeletonHealth = 100
CorruptedWolvesHealth = 150
ErrorSpritesHealth = 200
GlitchGolemsHealth = 250
ShadowKnightsHealth = 300
FlameWisps = 350


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
    the_beginning() # First (the_beginning)

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
    tutorial() # Second (Tutorial)

def tutorial():
    print()
    print("----------------------------------------")
    time.sleep(t)
    print("OVERVIEW/TUTORIAL")
    time.sleep(t)
    print("1. OBJECTIVE:")
    print("   - Your mission is to defeat opponents, solve puzzles, and conquer errors that plague the land.")
    print("   - Your choices matter! Pay attention to the story and options presented.")
    time.sleep(t)
    print("2. INTERACTIONS:")
    print("   - Use simple text-based commands to explore and interact.")
    print("   - Type commands like 'look', 'attack', 'inventory', or other prompts as needed.")
    time.sleep(t)
    print("3. INVENTORY:")
    print("   - Your inventory holds important items you acquire on your journey.")
    print("   - Check your inventory by typing 'inventory or i'. You can carry up to 4 items.")
    time.sleep(t)
    print("4. HEALTH:")
    print("   - Your health starts at 100. Make smart decisions to avoid losing it.")
    print("   - Keep an eye on your health as it determines how long you can survive.")
    time.sleep(t)
    print("5. CURRENCY:")
    print("   - Earn currency by completing tasks and defeating enemies.")
    print("   - Use currency to buy items or upgrade your abilities (later in the game).")
    time.sleep(t)
    print("6. SAVE/EXIT:")
    print("   - This version of the game doesn’t save progress automatically. Play smart!")
    print("   - You can exit the game anytime by typing 'exit' (but progress will be lost).")
    print("----------------------------------------")
    time.sleep(t*4)
    print()
    input("Press any key to continue: ")
    print()
    first_encounter()

def first_encounter():
    time.sleep(t)
    print("You start walking from the wise mans hut.")
    time.sleep(t)
    print("You end-up in a forest.")
    time.sleep(t)
    print("All of a sudden you hear git branch cracking and you see failed merge...")
    time.sleep(t)
    while(True):
        print()
        print("----------------------------------------")
        print(f"Player: {username}                                              Enemy: Skeleton")
        print(f"Health: {health}                                                Health: {skeletonHealth}")
        print()
        print()
        print()
        print("Your choises:")
        print("1. Attack    2. Runaway")
        print("----------------------------------------")
        choise = input(">")

game_start() # Starts game