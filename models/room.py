# models/room.py
from models.inventory import Inventory

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Updated to use a dictionary for exits
        self.items = Inventory()  # Using Inventory class for items
        self.actions = []  # List of actions available in the room

    def connect_room(self, room, direction):
        self.exits[direction] = room

    def add_item(self, item, quantity=1):
        self.items.add_item(item, quantity)

    def describe(self, player):
        print(f"{self.name}\n{self.description}")
        if player.has_ability("observation"):
            # Display exits and items using observation ability
            print("Exits: " + ", ".join(self.exits.keys()))
            self.items.show_inventory()  # Show items using Inventory's method

    def look_around(self):
        # Display exits
        print("Exits: " + ", ".join(self.exits.keys()))
        # Display items
        self.items.show_inventory()  # Show items using Inventory's method

    def set_actions(self, actions):
        self.actions = actions

    def perform_action(self, action, player):
        # This method should be implemented based on the game logic for actions
        pass

    def get_item_by_name(self, name):
        # Adjusted to work with the Inventory class
        return self.items.get_item(name)

    def remove_item(self, item_name):
        # Adjusted to work with the Inventory class
        return self.items.remove_item(item_name)
