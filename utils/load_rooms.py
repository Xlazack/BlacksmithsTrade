import json
from models.room import Room

def load_rooms(filepath='data/rooms.json', items={}):
    with open(filepath, 'r') as file:
        rooms_data = json.load(file)

    rooms = {}
    # First pass to create all room instances
    for room_name, room_info in rooms_data.items():
        room = Room(room_name, room_info["description"])
        # Loading items into rooms
        for item_name, item_info in room_info['items'].items():
            item = items.get(item_name)  # Retrieve the item template from global items
            if item:
                room.add_item(item, item_info['quantity'])
        room.set_actions(room_info.get("actions", []))  # Assuming Room class can store actions list
        rooms[room_name] = room

    # Second pass to establish room connections
    for room_name, room_info in rooms_data.items():
        room = rooms[room_name]
        for direction, connected_room_name in room_info.get("exits", {}).items():
            if connected_room_name in rooms:  # Ensure the connected room exists
                room.connect_room(rooms[connected_room_name], direction)
    
    return rooms
