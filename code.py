begining = input('Welcome! Please type Start to begin!').strip().lower()
if begining == "start":
    print('You wake up in a mysterious forest you have never seen before,' 
    ' you have no idea'  
    ' how you got there.')
  #first choice
    """Provide the player with initial options and return their choice"""
    while True:
        print("What do you do?")
        print("A = Explore the forest")
        print("B = Cry")
        print("C = Scream for help")
        choice = input("> ").strip().lower()
        if choice in ['a', 'b', 'c']:
            return choice
        else:
            print("Invalid input. Please type A, B, or C.")
            if choice= "a": print('test')
            
        
