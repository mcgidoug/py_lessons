import random
import string

print("Welcome to the Password Generator!")

# Ask the user how long they want the password to be
length = int(input("How long should your password be? (Between 4 and 12): "))

# Define possible characters
letters = string.ascii_letters  # a-z and A-Z
numbers = string.digits         # 0-9
symbols = "!@#$%&*"

# Combine all options into one list
all_chars = letters + numbers + symbols

# Create the password
password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Your new password is:", password)

