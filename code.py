# Start the game
beginning = input("Welcome! Please type Start to begin: ").strip().lower()

if beginning == "start":
    print(
        "You wake up in a mysterious forest you have never seen before. "
        "You have no idea how you got there."
    )

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
                choice_two(choice)# Pass the choice to the next function
                break
            else:
                print("Invalid input. Please type A, B, or C.")

    # Second choice function
    def choice_two(first_choice):
        """Handle the outcome of the first choice"""
        if first_choice == "a":
            print("You find a map with a marked path to a casle.")
            choice_three()
        elif first_choice == "b":
            print("test.")
        elif first_choice == "c":
            print("test.")

    # Start the first choice
    choice_one()

else:
    print("Please type start.")
def choice_three()
def choice_three():
    """Third scene: new set of choices"""
    while True
    print('test')
            
        
