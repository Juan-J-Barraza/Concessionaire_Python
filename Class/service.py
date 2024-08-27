
class Service:
    def __init__(self, name=None, address=None, NIF=None):
        self.name = name
        self.address = address
        self.NIF = NIF

    def __str__(self):
        return f"Service{{name='{self.name}, NIF={self.NIF}'}}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_NIF(self):
        return self.NIF

    def set_NIF(self, NIF):
        self.NIF = NIF
