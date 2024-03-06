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

    def describe(self):
        print(f"{self.name}\n{self.description}")
        if self.items:
            print("You see the following items: " + ", ".join(item.name for item in self.items))

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None

    def remove_item(self, item):
        self.items.remove(item)