
class Inventory:
    def __init__(self, location=None):
        self.location = location
        self.location_services = [] if location else None
        self.list_cars = []

    def __str__(self):
        return f"Inventory(list_cars={self.list_cars}, location={self.location}, location_services={self.location_services})"

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_location_services(self):
        return self.location_services

    def set_location_services(self, location_services):
        self.location_services = location_services

    def get_list_cars(self):
        return self.list_cars

    def set_list_cars(self, list_cars):
        self.list_cars = list_cars

    def add_service(self, service):
        self.location_services.append(service)
    
    def add_cars(self, cars):
        self.list_cars.append(cars)