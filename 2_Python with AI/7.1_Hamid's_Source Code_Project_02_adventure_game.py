# Step 1 - The game starts by introducing the player's quest and asking for their name.

def start_game():
    """Display game introduction and get player name"""
    print("\n" + "="*60)
    print("Welcome to the Treasure Quest Adventure!")
    print("="*60)
    print("\nYou are an explorer searching for legendary treasure")
    print("hidden in an ancient land. Your choices will determine")
    print("your success or failure.\n")
    
    player_name = input("What is your name, adventurer? ")
    print(f"\nGreat, {player_name}! Your quest begins now...\n")
    
# Step 2 - The player is given an initial choice of exploring different paths (a Dark Forest or a Mysterious Cave).
    """Initial choice"""
    print("You stand at a crossroads:")
    print("1. Enter the Dark Forest")
    print("2. Enter the Mysterious Cave")
    
    choice = input("\nChoose your path (1 or 2): ")
    
    if choice == "1":
        forest_path(player_name)
    elif choice == "2":
        cave_path(player_name)
    else:
        print("Invalid choice. Game over!")

# Step 3 - Crossroads Choice 1/2: will trigger the event for Forest Path leading to more decisions.

def forest_path(player_name):
    """Handle the forest scenario with player choices"""
    print(f"\n{player_name}, you enter the dense, dark forest...")
    print("The trees tower above you, blocking out the sunlight.")
    print("You hear a gentle sound of flowing water nearby.\n")
    
    print("What do you do?")
    print("1. Follow the river")
    print("2. Climb a tall tree to get your bearings")
    
    choice = input("\nChoose your action (1 or 2): ")
    
# Step 4 - Forest Path Choice 1/2: will trigger the event for River Path leading to winning the game. 

    if choice == "1":
        print(f"\n{player_name}, you follow the river downstream...")
        print("After hours of walking, you discover an ancient temple!")
        print("Inside, you find the legendary treasure chest!")
        print("\n🎉 CONGRATULATIONS! You found the treasure and won the game! 🎉\n")
        play_again()

# Step 5 - Forest Path Choice 2/2: will trigger a game over scenario. 

    elif choice == "2":
        print(f"\n{player_name}, you climb the tree...")
        print("From the top, you see a dark cave in the distance.")
        print("You slip while climbing down and get injured.")
        print("\n💀 Game Over! You were too injured to continue your quest. 💀\n")
        play_again()
    else:
        print("Invalid choice. Game over!")

# Step 6 - Crossroads Choice 2/2: will trigger the event for Cave Path leading to more decisions.

def cave_path(player_name):
    """Handle the cave scenario with player choices"""
    print(f"\n{player_name}, you enter the mysterious cave...")
    print("The air is cold and damp. Your eyes slowly adjust to the darkness.\n")
    
    print("You see two tunnels:")
    print("1. Take the left tunnel (narrow and dark)")
    print("2. Take the right tunnel (with a faint light)")
    
    choice = input("\nChoose your tunnel (1 or 2): ")
    
# Step 7 - Cave Path Choice 1/2: will trigger a game over scenario.

    if choice == "1":
        print(f"\n{player_name}, you venture into the left tunnel...")
        print("It becomes increasingly narrow. You get stuck!")
        print("\n💀 Game Over! You are trapped in the darkness. 💀\n")
        play_again()
        
# Step 8 - Cave Path Choice 2/2: will trigger the event for Light Tunnel leading to winning the game.

    elif choice == "2":
        print(f"\n{player_name}, you follow the light...")
        print("The tunnel opens into a grand chamber!")
        print("There it is - the legendary treasure chest, glowing with ancient magic!")
        print("\n🎉 CONGRATULATIONS! You found the treasure and won the game! 🎉\n")
        play_again()
    else:
        print("Invalid choice. Game over!")

# Step 9 - After reaching an ending, the player is prompted to restart or exit the game.

def play_again():
    """Ask if player wants to restart the game"""
    choice = input("Do you want to play again? (yes/no): ").lower()
    
    if choice == "yes" or choice == "y":
        start_game()
    else:
        print("\nThanks for playing! Goodbye!\n")

# Run the game
start_game()