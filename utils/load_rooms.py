import json
from models.room import Room

def load_rooms(filepath='data/rooms.json', items={}):
    with open(filepath, 'r') as file:
        rooms_data = json.load(file)
    
    rooms = {}
    for room_name, room_info in rooms_data.items():
        room = Room(room_name, room_info["description"])
        for item_name in room_info["items"]:
            if item_name in items:
                room.add_item(items[item_name])
        rooms[room_name] = room
    
    # After all rooms are created, establish their connections
    for room_name, room_info in rooms_data.items():
        room = rooms[room_name]
        for connection_name, connected_room_name in room_info.items():
            # Check if connection_name is a valid direction or named destination
            if connection_name in ["north", "south", "east", "west", "forest", "home", "forge"] and connected_room_name in rooms:
                # Connect rooms based on the provided direction/named destination
                room.connect_room(rooms[connected_room_name], connection_name.lower())
    
    return rooms