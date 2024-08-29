

class Car:
    def __init__(self, frame_number=None, price=None, discount=None, technical_data=None, power=None, brand=None, models=None, status=None, features=None, concessionaire=None):
        self.frame_number = frame_number
        self.price = price
        self.discount = discount
        self.technical_data = technical_data
        self.power = power
        self.brand = brand
        self.models = models
        self.status = status
        self.features = features
        self.concessionaire = concessionaire
        self.list_equipments = []
        self.list_available_extras = []

    def __str__(self):
        equipment = ', '.join([equipment.name for equipment in self.list_equipments])
        extra = ', '.join([f"{extra.name} (${extra.price})" for extra in self.list_available_extras])
        return f"Car(model='{self.models}', price={self.price}, brand='{self.brand}', status='{self.status}', power='{self.power}', features='{self.features}', list_equipments=[{equipment}], extra_equipments=[{extra}])"
             

        

    def get_frame_number(self):
        return self.frame_number

    def set_frame_number(self, frame_number):
        self.frame_number = frame_number

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_technical_data(self):
        return self.technical_data

    def set_technical_data(self, technical_data):
        self.technical_data = technical_data

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def get_brand(self):
        return self.brand

    def set_brand(self, brand):
        self.brand = brand

    def get_models(self):
        return self.models

    def set_models(self, models):
        self.models = models

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_features(self):
        return self.features

    def set_features(self, features):
        self.features = features      
    
    def get_concessionaire(self):
        return self.concessionaire
    
    def set_concesssionaire(self, concessionaire):
        self.concessionaire = concessionaire  

    def get_list_equipments(self):
        return self.list_equipments

    def set_list_equipments(self, list_equipments):
        self.list_equipments = list_equipments

    def get_list_available_extras(self):
        return self.list_available_extras

    def set_list_available_extras(self, list_available_extras):
        self.list_available_extras = list_available_extras

    def add_equipment(self, equipment):
        self.list_equipments.append(equipment)

    def add_extra(self, extra):
        self.list_available_extras.append(extra)
