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
            outcome_1(choice)
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Handle first choice
def outcome_1(first_choice):
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
            outcome_2(choice)
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
            outcome_3
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
            outcome_4
        else:
            print("Invalid input. Please type A, B, or C.")

# Outcome after map decision
def outcome_2(second_choice):
    if second_choice == "a":
        print("You follow the map and get to the castle.")
    elif second_choice == "b":
        print("You put the map back but something doesn't feel right.")
    elif second_choice == "c":
        print("You put the map in your backpack.")

# Placeholder for another branch
def outcome_3(third_choice):
    if third_choice == "a":
        print("You find a map with a marked path to a castle.")
        choice_two(third_choice)
    elif third_choice == "b":
        print("You wander aimlessly and get lost.")
    elif third_choice == "c":
        print("You sit and sing until night falls.")

def outcome_4(fourth_choice):
    if choice_four == "a":
        print("You find a map with a marked path to a castle.")
    elif choice_four == "b":
        print("You sit down and cry. Nothing changes.")
    elif choice_four == "c":
        print("You wander aimlessly and get lost.")

        
    


 

# Game start logic
if beginning == "start":
    print("You wake up in a mysterious forest you have never seen before. "
          "You have no idea how you got there.")
    choice_one()
else:
    print("Game not started.")

