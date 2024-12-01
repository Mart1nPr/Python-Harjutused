# Password generator
# 12/1/2024

import random

password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"

length = int(input("Enter a number for the password length (8-30): "))
if length < 8 or length > 30:
    print("Choose in range (8-30)")
else:
    for i in range(length):
        randomCharacter = random.choice(characters)
        password += randomCharacter
    print("Your new password is: ", password)
    

