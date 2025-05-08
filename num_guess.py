import random

num = random.randint(1,3)
attempts = 3

while attempts > 0:
    question = int(input(f"What is the number? You have {attempts} attempts left. "))

    if question == num:
        print(f"NICE! You completed with {attempts -1} attempts left")
        break

    attempts -= 1

    if attempts ==0:
        print("Game over!")

    
    else:
        print(f"Try again... {attempts} attempts left.")
