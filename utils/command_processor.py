# command_processor.py
from utils.functions import wait_for_key_press, clear_screen
from utils.state_manager import GameState

def process_command(command, current_state, player, time_system):
    if current_state == GameState.EXPLORING:
        if command[0] == "go" and len(command) > 1:
            destination = command[2] if len(command) >= 3 and command[1] == "to" else command[1]
            destination = destination.lower()

            if destination in player.current_location.connected_rooms:
                new_room_key = player.current_location.connected_rooms[destination]
                player.move_to(new_room_key)
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
        elif (command[0] == "look" and len(command) > 1 and command[1] == "around") or (command[0] == "la"):
            player.current_location.look_around()
            wait_for_key_press()

    elif current_state == GameState.INVENTORY:
        if command[0] == "inspect" and len(command) > 1:
            item_name = " ".join(command[1:])
            player.inspect_item(item_name)
            wait_for_key_press()
        else:
            print("Invalid command.")
            wait_for_key_press()
