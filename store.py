from item import Item

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(item.title, 'was added')
