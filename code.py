# Start the game
beginning = input("Welcome! Please type Start to begin: ").strip().lower()

# First choice function
def choice_one():
    """Provide the player with initial options and return their choice"""
    while True:
        print("\nWhat do you do?")
        print("A = Explore the forest")
        print("B = Cry")
        print("C = Scream for help")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_1  # Pass the choice to the next function
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Second choice function
def outcome_1(first_choice):
    """Handle the outcome of the first choice"""
    if first_choice == "a":
        print("You find a map with a marked path to a castle.")
        choice_two(first_choice)
    elif first_choice == "b":
        print("You sit down and cry. Nothing changes.")
        choice_three(first_choice)
    elif first_choice == "c":
        print("You scream for help, but no one answers.")
        choice_four(first_choice)

# second choice function
def choice_two(previous_choice):
    """Second stage after finding the map"""
    while True:
        print("\nWhat do you do?")
        print("A = Follow the map")
        print("B = Put the map back")
        print("C = Keep the map but not follow it")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            print(f"You chose option {choice.upper()} after finding the map.")
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# third choice function
def choice_three(previous_choice):
    """Second stage after crying"""
    while True:
        print("\nWhat do you do?")
        print("A = Explore the forest")
        print("B = Walk mindlessly")
        print("C = Sit there and sing")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            print(f"You chose option {choice.upper()} after crying") # Pass the choice to the next function
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# fourth choice function
def choice_four(previous_choice):
    """Second stage after calling for help"""
    while True:
        print("\nwhat do you do?")
        print("A = Explore the forest")
        print("B = cry")
        print("C = Walk mindlessly")
# Game start logic
if beginning == "start":
    print("You wake up in a mysterious forest you have never seen before. "
          "You have no idea how you got there.")
    choice_one()
else:
    print("Game not started.")
