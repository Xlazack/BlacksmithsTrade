class Inventory:
    def __init__(self):
        self.items = {}  # Holds unique items and quantities

    def add_item(self, item, quantity=1):
        # Check if item is stackable and update quantity or add as a new entry
        if item.stackable:
            if item.name in self.items:
                self.items[item.name]['quantity'] += quantity
            else:
                self.items[item.name] = {'item': item, 'quantity': quantity}
        else:
            # Unique items get a unique entry based on their ID
            self.items[item.id] = {'item': item, 'quantity': 1}

    def remove_item(self, item_name):
        # Attempt to remove from bulk items first
        if item_name in self.bulk:
            self.bulk[item_name]['quantity'] -= 1
            if self.bulk[item_name]['quantity'] <= 0:
                del self.bulk[item_name]  # Remove the entry if quantity drops to 0
            return True
        # If not a bulk item, search unique items
        for id, item in self.items.items():
            if item.name == item_name:
                del self.items[id]  # Remove the item by ID
                return True
        return False  # Item not found

    def get_item(self, item_name):
        # Check bulk items
        if item_name in self.bulk:
            return self.bulk[item_name]['item']
        # Check unique items
        for item in self.items.values():
            if item.name == item_name:
                return item
        return None  # Item not found

    def show_inventory(self):
        print("Inventory:")
        if not self.items and not self.bulk:
            print("  Empty")
        for item in self.items.values():
            print(f"  {item.name} (Unique Item)")
        for item_name, info in self.bulk.items():
            print(f"  {info['quantity']} {item_name}")