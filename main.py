# main.py
from models.player import Player
from utils.functions import clear_screen
from utils.load_items import load_items
from utils.load_rooms import load_rooms
from utils.help import show_help
from utils.main_menu import show_title_screen
from utils.functions import wait_for_key_press
from utils.definitions import GameState
from utils.command_processor import process_command
from utils.state_manager import StateManager
from utils.game_systems import TimeSystem

global_items = None

def setup_game():
    global global_items
    items = load_items()
    global_items = items  # Set the global variable
    rooms = load_rooms(items=items)
    time_system = TimeSystem()
    starting_room = rooms["Living Room"]  # Assuming you start in the Living Room
    player = Player(starting_room)
    return player, time_system


def main():
    player, time_system = setup_game()
    state_manager = StateManager()  # Initialize the state manager
    show_title_screen()

    while True:
        # Update: Using state_manager to get and set current state
        current_state = state_manager.get_current_state()

        # Move clear_screen() to later in the loop
        if current_state == GameState.EXPLORING:
            player.current_location.describe(player)
        elif current_state == GameState.INVENTORY:
            player.show_inventory()
        
        command = input("> ").lower().split()

        # Check for empty command and continue the loop if nothing is entered
        if not command:
            continue
        # Check for universal commands
        if command[0] in ["quit", "exit"]:
            print("Bye, have a great time!")
            break
        elif command[0] == "help":
            show_help(current_state)
            wait_for_key_press()
        elif command[0] in ["inventory", "inv"]:
            state_manager.set_current_state(GameState.INVENTORY)
        elif command[0] in ["back", "b"]:
            state_manager.set_current_state(GameState.EXPLORING)
        else:
            process_command(command, current_state, player, time_system)
            

        clear_screen()

if __name__ == "__main__":
    main()