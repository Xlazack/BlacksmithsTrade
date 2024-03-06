# models/room.py
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_rooms = {}
        self.items = []

    def connect_room(self, room, direction):
        self.connected_rooms[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def describe(self, player):
        print(f"{self.name}\n{self.description}")
        if player.has_ability("observation"):
            # Logic to display room exits
            print("Exits: " + ", ".join(self.connected_rooms.keys()))
            # Logic to display items
            if self.items:
                print("You see the following items: " + ", ".join(item.name for item in self.items))

    def look_around(self):
        # Logic to display room exits
        print("Exits: " + ", ".join(self.connected_rooms.keys()))
        # Logic to display items
        if self.items:
            print("You see the following items: " + ", ".join(item.name for item in self.items))
        else:
            print("You don't see any items around.")

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def remove_item(self, item):
        self.items.remove(item)