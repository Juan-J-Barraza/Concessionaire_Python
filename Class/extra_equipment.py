

class ExtraEquipment:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __str__(self):
        return f"ExtraEquipment(name='{self.name}', price='{self.price}')"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
