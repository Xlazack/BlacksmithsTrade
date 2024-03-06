import json
from models.item import Item

def load_items(filepath='data/items.json'):
    with open(filepath, 'r') as file:
        items_data = json.load(file)
    
    items = {}
    for item_name, item_info in items_data.items():
        # Join the lines of the ASCII image with newline characters if it exists
        image = "\n".join(item_info["image"]) if "image" in item_info else None
        description = item_info["description"]
        
        # Combine the description and the image, if there is one
        full_description = f"{description}\n{image}" if image else description
        
        items[item_name] = Item(item_name, full_description)
    
    return items