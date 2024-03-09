# models/player.py
from models.inventory import Inventory

class Player:
    def __init__(self, start_location):
        self.current_location = start_location
        self.inventory = Inventory()  # Initializes the new Inventory object
        self.abilities = {"observation": False}

    def has_ability(self, ability_name):
        return self.abilities.get(ability_name, False)

    def pick_up_item(self, item, quantity=1):
        self.inventory.add_item(item, quantity)  # Use Inventory's add_item method
        print(f"You picked up {quantity} {item.name}.")

    def drop_item(self, item_name):
        # This method needs significant adjustments for the new inventory system
        item_dropped = self.inventory.remove_item(item_name)  # Assume Inventory has a remove_item method
        if item_dropped:
            print(f"You dropped {item_name}.")
            self.current_location.add_item(item_dropped)  # Assume locations can also handle items
        else:
            print("You don't have that item.")

    def show_inventory(self):
        self.inventory.show_inventory()  # Delegate to Inventory's show_inventory method

    def inspect_item(self, item_name):
        item = self.inventory.get_item(item_name)  # Assume Inventory has a get_item method
        if item:
            print(item.description)  # Example of using an Item attribute
        else:
            print("You don't have that item in your inventory.")

    def move_to(self, new_location):
        self.current_location = new_location