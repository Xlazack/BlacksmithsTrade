import json
from models.item import Item
from models.item import UniqueItem


def load_items(filepath='data/items.json'):
    with open(filepath, 'r') as file:
        items_data = json.load(file)

    items = {}
    for item_name, item_info in items_data.items():
        image = "\n".join(item_info["image"]) if "image" in item_info else None
        description = item_info["description"]
        full_description = f"{description}\n{image}" if image else description

        if ('enchantments' in item_info) or ('properties' in item_info):
            # Create a UniqueItem if enchantments are present
            item = UniqueItem(
                name=item_name,
                item_type=item_info["type"],
                description=item_info["description"],
                stackable=item_info.get("stackable", False),
                properties=item_info.get("properties", {}),
                enchantments=item_info["enchantments"]
            )
        else:
            # Create a regular Item otherwise
            item = Item(
                name=item_name,
                item_type=item_info["type"],
                description=item_info["description"],
                stackable=item_info.get("stackable", False)
            )
        items[item_name] = item

    return items
