
class TypeConcessionaire:
    def __init__(self, brand=None, concesionarie=None, car=None):
        self.brand = brand
        self.concesionarie = concesionarie
        self.car = car

    def __str__(self):
        concesionarie_name = self.concesionarie.name if self.concesionarie else None
        car_model = self.car.models if self.car else None
        return (f"TypeConcessionaire{{brand='{self.brand}', "
                f"concesionarie='{concesionarie_name}', car='{car_model}'}}")

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_concesionarie(self):
        return self.concesionarie

    def set_concesionarie(self, concesionarie):
        self.concesionarie = concesionarie

    def get_car(self):
        return self.car

    def set_car(self, car):
        self.car = car
