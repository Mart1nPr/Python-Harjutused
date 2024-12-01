# Text adventure game
# The Serpent's Legacy

inventory = []
currency = 0
username = ""
health = 100

def start_game():
    global username
    print("The Serpent's Legacy")
    print()
    print("Welcome to the The Serpent's Legacy text adventure game!")
    print("Your goal is to slay the dragon that rules the ancient ruins of Drakmor")
    username = input("Enter your username: ")

start_game()

