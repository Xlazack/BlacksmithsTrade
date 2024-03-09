# models/item.py
import uuid

class Item:
    def __init__(self, name, description="", properties=None, enchantments=None, stackable=False, item_type =None):
        self.id = uuid.uuid4() if not stackable else name  # Use name as ID for stackable items
        self.name = name
        self.description = description
        self.properties = properties if properties else {}
        self.enchantments = enchantments if enchantments else {}
        self.stackable = stackable
        self.item_type = item_type

    def __str__(self):
        enchanted_properties = ', '.join([f"{k}: {v}" for k, v in self.enchantments.items()])
        return f"{self.name} (Type: {self.item_type}, {'Enchanted with ' + enchanted_properties if enchanted_properties else 'No enchantments'})"
