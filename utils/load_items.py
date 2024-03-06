import json
from models.item import Item

def load_items(filepath='data/items.json'):
    with open(filepath, 'r') as file:
        items_data = json.load(file)
    
    items = {}
    for item_name, item_info in items_data.items():
        items[item_name] = Item(item_name, item_info["description"])
    
    return items