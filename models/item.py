# models/item.py
import uuid

class Item:
    def __init__(self, name, item_type, description, stackable, properties=None, enchantments=None):
        self.id = uuid.uuid4()  # Unique identifier for unique items
        self.name = name
        self.type = item_type
        self.description = description
        self.stackable = stackable
        self.properties = properties if properties else {}
        self.enchantments = enchantments if enchantments else {}

class UniqueItem(Item):  # Extended class for unique items
    def __init__(self, name, item_type, description, properties, enchantments):
        super().__init__(name, item_type, description, stackable=False)
        self.properties = properties  # Additional properties dict for unique items
        self.enchantments = enchantments