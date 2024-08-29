

class Concessionaire:
    
    def __init__(self, name=None, NIT=None):
        self.name = name
        self.NIT = NIT
        self.list_services = []
        self.list_sellers = []
        self.list_cars = []
    
    def __str__(self):
        sellers = ', '.join([seller.name for seller in self.list_sellers])
        return f"Concessionaire(name={self.name}, NIT={self.NIT}, list_sellers=[{sellers}])"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_NIT(self):
        return self.NIT

    def set_NIT(self, NIT):
        self.NIT = NIT

    def get_list_services(self):
        return self.list_services

    def set_list_services(self, list_services):
        self.list_services = list_services

    def get_list_sellers(self):
        return self.list_sellers

    def set_list_sellers(self, list_sellers):
        self.list_sellers = list_sellers
        
    def get_list_cars(self):
        return self.list_cars
    
    def set_listt_cars(self, list_cars):
        self.list_cars = list_cars
    
    def add_service(self, service):
        self.list_services.append(service)

    def add_sellers(self, seller):
        self.list_sellers.append(seller)
        
    def add_cars(self, car):
        self.list_cars.append(car)
