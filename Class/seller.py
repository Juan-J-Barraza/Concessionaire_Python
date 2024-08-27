
class Seller:
    def __init__(self, name=None, last_name=None, NIF=None, address=None):
        self.name = name
        self.last_name = last_name
        self.NIF = NIF
        self.address = address
        self.list_clients = []
        self.list_sales = []
    
    def __str__(self):
        return f"Seller(name={self.name}, last_name={self.last_name}, NIF={self.NIF}, list_clients={self.list_clients}, list_sales={self.list_sales})"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_NIF(self):
        return self.NIF

    def set_NIF(self, NIF):
        self.NIF = NIF

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_list_clients(self):
        return self.list_clients

    def set_list_clients(self, list_clients):
        self.list_clients = list_clients

    def get_list_sales(self):
        return self.list_sales

    def set_list_sales(self, list_sales):
        self.list_sales = list_sales
    
    def add_clients(self, clients):
        self.list_clients.append(clients)
    
    def add_sales(self, sales):
        self.list_sales.append(sales)