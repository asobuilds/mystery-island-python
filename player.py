STARTING_ENERGY = 7


class Player:
    def __init__(self, name):
        self.name = name
        self.energy = STARTING_ENERGY
        self.inventory = []
        self.current_scene = "beach"

    def has_item(self, item):
        return item in self.inventory

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
