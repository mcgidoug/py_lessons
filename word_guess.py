import random

words = ["dog", "cat", "mouse", "elephant"]
word = random.choice(words)
attempts = 3

while attempts > 0:
    guess = input(f"What is the word? You have {attempts} attempts left: ").strip().lower()

    if guess == word:
        print(f"NICE! You got it with {attempts - 1} attempts left!")
        break

    attempts -= 1

    if attempts == 0:
        print(f"Game over! The word was: {word}")
    else:
        print("Try again...")

