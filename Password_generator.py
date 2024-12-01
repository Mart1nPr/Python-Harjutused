# Password generator

import random

password = ""
randomLetter = "abcdefghijklmnopqrstuvwxyz"

length = int(input("Enter a number for the password length (min 5 / max 9): "))

for i in range(length):
    randomLet = random.choice(randomLetter)
    case = True
    password += case

print("Your new password is: ", password)
    

