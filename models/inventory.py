class Inventory:
    def __init__(self):
        self.stackable_items = {}  # Use for items that can be stacked (quantities)
        self.unique_items = {}  # Use for unique items, keyed by item ID

    def add_item(self, item, quantity=1):
        if item.stackable:
            # For stackable items, update quantity
            if item.name in self.stackable_items:
                self.stackable_items[item.name]['quantity'] += quantity
            else:
                self.stackable_items[item.name] = {'item': item, 'quantity': quantity}
        else:
            # Unique items are stored directly by their ID
            self.unique_items[item.id] = item

    def remove_item(self, item_name):
        # Try removing a stackable item first
        if item_name in self.stackable_items:
            self.stackable_items[item_name]['quantity'] -= 1
            if self.stackable_items[item_name]['quantity'] <= 0:
                del self.stackable_items[item_name]  # Remove if no more left
            return True
        # If not found, try removing a unique item by name
        for id, item in self.unique_items.items():
            if item.name == item_name:
                del self.unique_items[id]  # Remove the unique item
                return True
        return False  # Item not found

    def get_item(self, item_name):
        # Look for a stackable item first
        if item_name in self.stackable_items:
            return self.stackable_items[item_name]['item']
        # Look for a unique item by name
        for item in self.unique_items.values():
            if item.name == item_name:
                return item
        return None  # Item not found

    def show_inventory(self):
        print("Inventory:")
        if not self.stackable_items and not self.unique_items:
            print("  Empty")
        else:
            # Display stackable items and their quantities
            for item_name, info in self.stackable_items.items():
                print(f"  {info['quantity']} x {item_name}")
            # Display unique items
            for item in self.unique_items.values():
                print(f"  {item.name} (Unique Item)")