# command_processor.py
from utils.functions import wait_for_key_press, clear_screen
from utils.state_manager import GameState

def process_command(command, current_state, player, time_system):
    # Exploring
    if current_state == GameState.EXPLORING:
        # Command "go to"
        if command[0] == "go" and len(command) > 1:
            destination = command[2] if len(command) >= 3 and command[1] == "to" else command[1]
            destination = destination.lower()

            if destination in player.current_location.exits:
                new_room_key = player.current_location.exits[destination]
                player.move_to(new_room_key)
            else:
                print("You can't go that way.")
                wait_for_key_press()
        # Command "pick up"
        elif command[0] == "pick" and len(command) > 2 and command[1] == "up":
            item_name = " ".join(command[2:])
            item = player.current_location.get_item_by_name(item_name)
            if item:
                player.pick_up_item(item)
                player.current_location.remove_item(item)
            else:
                print("You don't see that item here.")
                wait_for_key_press()
        # Command "look around"
        elif (command[0] == "look" and len(command) > 1 and command[1] == "around") or (command[0] == "la"):
            player.current_location.look_around()
            wait_for_key_press()
        # Command gather wood
        elif player.current_location.name == "Forest" and command[0] == "gather" and len(command) > 1 and command[1] == "wood":
            # Perform the action of gathering wood
            time_system.advance_time(1)  # This action takes 1 hour
            # Assuming you have a global or accessible object that stores items, e.g., game_items
            wood_item = global_items.get("Wood")  # Retrieve the "Wood" item
            if wood_item:  # Check if "Wood" item is found
                wood_amount = 4  # Define how much wood is gathered
                player.pick_up_item(wood_item, wood_amount)
                print(f"You gather {wood_amount} sets of wood. It takes an hour.")
            else:
                print("Wood is not available.")
            
            wait_for_key_press()
        else:
            print("You can't do that here.")
            wait_for_key_press()

    # Inventory
    elif current_state == GameState.INVENTORY:
        if command[0] == "inspect" and len(command) > 1:
            item_name = " ".join(command[1:])
            player.inspect_item(item_name)
            wait_for_key_press()
        else:
            print("Invalid command.")
            wait_for_key_press()
