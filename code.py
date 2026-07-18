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
            outcome_1(choice)  # ✅ Correct function call
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

# Second stage after finding the map
def choice_two(previous_choice):
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

# Second stage after crying
def choice_three(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Explore the forest")
        print("B = Walk mindlessly")
        print("C = Sit there and sing")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            print(f"You chose option {choice.upper()} after crying.")
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Second stage after calling for help
def choice_four(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Explore the forest")
        print("B = Cry")
        print("C = Walk mindlessly")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            print(f"You chose option {choice.upper()} after calling for help.")
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Game start logic
if beginning == "start":
    print("You wake up in a mysterious forest you have never seen before. "
          "You have no idea how you got there.")
    choice_one()
else:
    print("Game not started.")
