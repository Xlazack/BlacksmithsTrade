# main.py
from models.player import Player
from models.room import Room
from models.item import Item
from utils.functions import clear_screen
from utils.load_items import load_items
from utils.load_rooms import load_rooms
from utils.commands import show_help
from utils.main_menu import show_title_screen
from utils.functions import wait_for_key_press
from utils.definitions import GameState

def setup_game():
    items = load_items()
    rooms = load_rooms(items=items)
    starting_room = rooms["Living Room"]  # Assuming you start in the Living Room
    player = Player(starting_room)
    return player

def process_command(command, current_state, player):
    if current_state == GameState.EXPLORING:
        if command[0] == "go" and len(command) > 1:
            direction = command[1]
            if direction in player.current_location.connected_rooms:
                player.move_to(player.current_location.connected_rooms[direction])
            else:
                print("You can't go that way.")
                wait_for_key_press()
        elif command[0] == "pick" and len(command) > 2 and command[1] == "up":
            item_name = " ".join(command[2:])
            item = player.current_location.get_item_by_name(item_name)
            if item:
                player.pick_up_item(item)
                player.current_location.remove_item(item)
            else:
                print("You don't see that item here.")
                wait_for_key_press()
        else:
            print("Invalid command.")
            wait_for_key_press()

    elif current_state == GameState.INVENTORY:
        if command[0] == "inspect" and len(command) > 1:
            item_name = " ".join(command[1:])
            clear_screen()
            player.inspect_item(item_name)
            wait_for_key_press()
        else:
            print("Invalid command.")
            wait_for_key_press()

def main():
    player = setup_game()
    current_state = GameState.EXPLORING
    show_title_screen()

    while True:
        # Move clear_screen() to later in the loop
        if current_state == GameState.EXPLORING:
            player.current_location.describe()
        elif current_state == GameState.INVENTORY:
            player.show_inventory()

        command = input("> ").lower().split()

        # The clear_screen() call is now moved after command processing
        # and only before the loop restarts, after player acknowledgement for certain commands

        if command[0] in ["quit", "exit"]:
            break
        elif command[0] == "help":
            show_help(current_state)
            input("Press Enter to continue...")  # Let player read the help output
        elif command[0] == "inventory":
            current_state = GameState.INVENTORY
        elif command[0] == "back":
            current_state = GameState.EXPLORING
        else:
            process_command(command, current_state, player)
        
        # Consider adding a general wait or clear screen prompt here, based on the command
        # For commands that need the user to read something before proceeding, call wait_for_key_press()
        clear_screen()

if __name__ == "__main__":
    main()