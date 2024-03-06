from utils.functions import clear_screen
from utils.functions import wait_for_key_press

def show_title_screen():
    clear_screen()
    print("Welcome to My Text Adventure Game!")
    print("1. Start Game")
    print("2. Load Game")
    print("3. About")
    print("4. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        clear_screen()
        start_game()
    elif choice == "2":
        clear_screen()
        print("Work in progress")#load_game()  # Placeholder for future implementation
        wait_for_key_press()
        show_title_screen()
    elif choice == "3":
        clear_screen()
        show_about()
    elif choice == "4":
        clear_screen()
        quit_game()
    else:
        clear_screen()
        print("Invalid option.")
        wait_for_key_press()
        show_title_screen()

def start_game():
    # Initialize your game here and then enter the game loop
    pass

def show_about():
    clear_screen()
    print("About this game...")
    # Add your game's backstory or information here
    wait_for_key_press()
    show_title_screen()

def quit_game():
    print("Thanks for playing!")
    exit()