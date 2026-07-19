# Start the game
beginning = input("Welcome! Please type Start to begin: ").strip().lower()

# First choice function
def choice_one():
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
            outcome_3(choice)
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
            outcome_4(choice)
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Outcome after map decision
def outcome_2(second_choice):
    if second_choice == "a":
        print("You follow the map and get to the castle.")
        choice_five(second_choice)
    elif second_choice == "b":
        print("You put the map back but something doesn't feel right.")
        choice_six(second_choice)
    elif second_choice == "c":
        print("You put the map in your backpack.")
        choice_seven(second_choice)

# Outcome after crying branch
def outcome_3(third_choice):
    if third_choice == "a":
        print("You find a map with a marked path to a castle.")
        choice_two(third_choice)
    elif third_choice == "b":
        print("You wander aimlessly and get lost.")
        choice_eight(third_choice)
    elif third_choice == "c":
        print("You sit and sing until night falls.")
        choice_nine(third_choice)

# Outcome after screaming branch
def outcome_4(fourth_choice):
    if fourth_choice == "a":
        print("You find a map with a marked path to a castle.")
        choice_two(fourth_choice)
    elif fourth_choice == "b":
        print("You sit down and cry. Nothing changes.")
        choice_three(fourth_choice)
    elif fourth_choice == "c":
        print("You wander aimlessly and get lost.")
        choice_eight(fourth_choice)

# Castle choices
def choice_five(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Walk in")
        print("B = Knock on the door")
        print("C = Explore the village")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_5(choice)
        else:
            print("Invalid input. Please type A, B, or C.")

# Put map back choices
def choice_six(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Pick the map back up and follow it")
        print("B = Walk mindlessly")
        print("C = Sit there and sing")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_6(choice)
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Keep map choices
def choice_seven(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Walk mindlessly")
        print("B = Sit there and sing")
        print("C = Use the map")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_7(choice)
        else:
            print("Invalid input. Please type A, B, or C.")

# Walk mindlessly
def choice_eight(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Keep walking")
        print("B = Sleep")
        print("C = Dance with no music")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_8(choice)
            break
        else:
            print("Invalid input. Please type A, B, or C.")

# Singing branch
def choice_nine(previous_choice):
    while True:
        print("\nWhat do you do?")
        print("A = Sleep")
        print("B = Dance with no music")
        print("C = Walk around")
        choice = input("> ").strip().lower()

        if choice in ['a', 'b', 'c']:
            outcome_9(choice)
            break
        else:
            print("Invalid input. Please type A, B, or C.")

def outcome_5(fifth_choice):
    if fifth_choice == "a":
        print("You walk in to what looks like a meeting of multiple diffrent cretures an elf looks at you and says 'we have been expecting you'")  
    if fifth_choice == "b":
        print(" A girl in a fancy dress and a crown opens the door and invites you inside saying 'I have been expecting you.'")  
    if fifth_choice == "c":
        print (" you walk around the village and find a market")

def outcome_6(sixth_choice):
    if sixth_choice == "a":
        print("you follow the map to the castle.")
    if sixth_choice == "b":
        print("You wander aimlessly and get lost.")
    if sixth_choice == "c":
         print("You sit and sing until night falls.")

def outcome_7(seventh_choice):
    if seventh_choice == "a":
        print("You wander aimlessly and get lost.")
    if seventh_choice == "b":
        print("You sit and sing until night falls.")
    if seventh_choice == "c":
        print("you follow the map to the castle.")

def outcome_8(eighth_choice):
    if eighth_choice == "a":
        print("You wander till you find a castle")
    if eighth_choice == "b":
     print("You sleep until the next day")
    if eighth_choice == "c":
        print("you dance until you hear somthing behind you")

def outcome_9(ninth_choice):
    if ninth_choice == "a":
        print("you sleep until the next day")
    if ninth_choice == "b":
        print("you dance until you hear somthing behind you")
    if ninth_choice == "c":
        print("You wander aimlessly and get lost.")

    








# Game start logic
if beginning == "start":
    print("You wake up in a mysterious forest you have never seen before. "
          "You have no idea how you got there.")
    choice_one()
else:
    print("Game not started.")


