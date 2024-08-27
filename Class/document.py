from datetime import datetime

class Document:
    def __init__(self, pay_method=None, date=None, client=None, car=None, seller=None):
        self.pay_method = pay_method
        self.date = date if date else datetime.now()
        self.client = client
        self.car = car
        self.seller = seller
        self.list_extra_equipments = []
        
    def __str__(self):
        return f"Docuemnt(pay_method={self.pay_method}, date={self.date}, client={self.client}, car={self.car}), seller={self.seller}"

    def get_pay_method(self):
        return self.pay_method

    def set_pay_method(self, pay_method):
        self.pay_method = pay_method

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_client(self):
        return self.client

    def set_client(self, client):
        self.client = client

    def get_list_extra_equipments(self):
        return self.list_extra_equipments

    def set_list_extra_equipments(self, list_extra_equipments):
        self.list_extra_equipments = list_extra_equipments

    def get_car(self):
        return self.car

    def set_car(self, car):
        self.car = car

    def get_seller(self):
        return self.seller

    def set_seller(self, seller):
        self.seller = seller

    def add_extra_equipment(self, extra):
        self.list_extra_equipments.append(extra)