from utils.definitions import GameState
from utils.functions import clear_screen


commands = {
    GameState.EXPLORING: {
        "look around": "Look around to see possible directions and items. Requires observation ability.",
        "go [direction]/go to [location]": "Move to a different area or room.",
        "pick up [item]": "Picks up an item from the current room.",
        "inventory": "Opens your inventory.",
        "help": "Displays this help message.",
        "quit": "Exits the game."
    },
    GameState.INVENTORY: {
        "inspect [item]": "Provides more information about an item in your inventory.",
        "back": "Returns to exploring.",
        "help": "Displays this help message.",
        "quit": "Exits the game."
    }
}


def show_help(current_state):
    clear_screen()
    print("Available commands:")
    for command, description in commands[current_state].items():
        print(f"{command}: {description}")