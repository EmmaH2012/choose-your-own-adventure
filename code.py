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
            choice_two(choice)  # Pass the choice to the next function
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Second choice function
def choice_two(first_choice):
    """Handle the outcome of the first choice"""
    if first_choice == "a":
        print("You find a map with a marked path to a castle.")
        choice_three(choice)
    elif first_choice == "b":
        print("You sit down and cry. Nothing changes.")
         choice_four(choice) # pyright: ignore[reportUndefinedVariable]
   
    elif first_choice == "c":
        print("You scream for help, but no one answers.")

# Third choice function (placeholder)
def choice_three(second_choice):
     """Provide the player with initial options and return their choice"""
    while True:
        print("\nWhat do you do?")
        print("A = Follow the map")
        print("B =  put the map back")
        print("C = keep the map but not follow it.")
        choice = input("> ").strip().lower()

def choice_four(second_choice):

         """Provide the player with initial options and return their choice"""
    while True:
        print("\nWhat do you do?")
        print("A = Explore the forest")
        print("B = Walk mindlessly")
        print("C = Sit there and sing")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            choice_two(choice)  # Pass the choice to the next function
            break
        else:
            print("Invalid input. Please type A, B, or C.")


        if choice in ['a', 'b', 'c']:
            (choice)  # Pass the choice to the next function
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
