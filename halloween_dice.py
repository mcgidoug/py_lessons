import random

print("🎃 Welcome to the Halloween Dice Roller!")
print("Roll the die and see what spooky surprise you get...\n")

input("Press ENTER to roll the die...")

roll = random.randint(1, 6)

if roll == 1:
    print("🍬 You got a piece of candy!")
elif roll == 2:
    print("🕷️ A spider crawled out of your bag! Eek!")
elif roll == 3:
    print("👻 A ghost flew through you! So cold!")
elif roll == 4:
    print("🧛‍♂️ A vampire gave you a high-five.")
elif roll == 5:
    print("🧙 You found a witch's hat!")
elif roll == 6:
    print("💀 You got cursed! You lose 1 candy!")

print("\nThanks for playing... Mwahahaha!")

