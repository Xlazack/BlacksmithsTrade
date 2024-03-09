import json
from models.item import Item


def load_items(filepath='data/items.json'):
    with open(filepath, 'r') as file:
        items_data = json.load(file)

    items = {}
    for item_name, item_info in items_data.items():
        image = "\n".join(item_info["image"]) if "image" in item_info else None
        description = item_info["description"]
        full_description = f"{description}\n{image}" if image else description

        # Extract item type from the JSON data
        item_type = item_info.get("type", None)  # Default to None if not specified

        item = Item(
            name=item_name,
            description=full_description,
            properties=item_info.get("properties", {}),
            enchantments=item_info.get("enchantments", {}),
            stackable=item_info.get("stackable", False),
            item_type=item_type  # Pass the item type
        )

        items[item_name] = item

    return items
