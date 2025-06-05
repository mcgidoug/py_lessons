def madlibs():
    print("Let's play Mad Libs!\n")

    # Get user input
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")

    # Story template
    story = f"""
    One day, a {adjective} {noun} was walking through the {place}.
    Suddenly, it {verb} very {adverb}.
    Out of nowhere, a wild {animal} appeared and chased the {noun} all the way home!
    What a crazy day!
    """

    print("\nHere's your Mad Libs story:")
    print(story)

# Run the game
madlibs()

