class Inventory:
    def __init__(self):
        self.stackable_items = {}  # Dictionary for stackable items with quantities
        self.unique_items = {}  # Dictionary for unique items, keyed by item ID

    def add_item(self, item, quantity=1):
        # For stackable items, update quantity or add as a new entry
        if item.stackable:
            if item.name in self.stackable_items:
                self.stackable_items[item.name]['quantity'] += quantity
            else:
                self.stackable_items[item.name] = {'item': item, 'quantity': quantity}
        # For unique items, add directly with their UUID
        else:
            self.unique_items[item.id] = item

    def remove_item(self, item_name, quantity=1):
        # Check if the item is stackable and exists
        if item_name in self.stackable_items:
            self.stackable_items[item_name]['quantity'] -= quantity
            # If the quantity drops to 0 or below, remove the item entry
            if self.stackable_items[item_name]['quantity'] <= 0:
                del self.stackable_items[item_name]
            return True
        # Handling unique items: since they are not stackable, ignore quantity for unique items
        # Note: This assumes unique item names or managing them via IDs instead
        for id, item in list(self.unique_items.items()):
            if item.name.lower() == item_name.lower():
                del self.unique_items[id]
                return True
        return False  # Item not found

    def get_item(self, item_name):
        # Check stackable items first
        if item_name in self.stackable_items:
            return self.stackable_items[item_name]['item']
        # Then check unique items by name, which is less efficient
        for item in self.unique_items.values():
            if item.name == item_name:
                return item
        return None  # Item not found

    def show_inventory(self):
        print("Inventory:")
        if not self.stackable_items and not self.unique_items:
            print("  Empty")
        else:
            for item_name, info in self.stackable_items.items():
                print(f"  {info['quantity']} x {item_name}")
            for id, item in self.unique_items.items():
                print(f"  Unique Item: {item.name}")
