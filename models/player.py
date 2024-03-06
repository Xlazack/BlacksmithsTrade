from utils.functions import wait_for_key_press
# models/player.py
class Player:
    def __init__(self, start_location):
        self.current_location = start_location
        self.inventory = []
        self.abilities = {"observation": True}#False}  # Start with all abilities not present

    def has_ability(self, ability_name):
        return self.abilities.get(ability_name, False)

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")

    def drop_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.current_location.add_item(item)
                print(f"You dropped {item.name}.")
                return
        print("You don't have that item.")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("You have the following items:")
            for item in self.inventory:
                print(item.name)

    def inspect_item(self, item_name):
        #print(f"Inspecting item: {item_name}")  # Debugging print
        #print(f"Current inventory: {[item.name for item in self.inventory]}")  # Debugging print
        #for item in self.inventory:
        #    if item.name.lower() == item_name.lower():
        #        print(item)
        #    return
        #print("You don't have that item in your inventory.")
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                print(item)
                return
        print("You don't have that item in your inventory.")

    def move_to(self, new_location):
        self.current_location = new_location
        
