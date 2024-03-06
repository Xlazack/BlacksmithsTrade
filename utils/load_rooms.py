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
    
    # Now that all rooms are created, connect them
    for room_name, room_info in rooms_data.items():
        for direction, connected_room_name in room_info.items():
            if direction in ["north", "south", "east", "west"] and connected_room_name in rooms:
                rooms[room_name].connect_room(rooms[connected_room_name], direction)
    
    return rooms