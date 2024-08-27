
class Sale:
    def __init__(self, registration=None, origin_car=None, document=None):
        self.registration = registration
        self.origin_car = origin_car
        self.document = document
    
    def __str__(self):
        return f"Sale(registration={self.registration}, origin_car={self.origin_car}, document={self.document})"

    def get_registration(self):
        return self.registration

    def set_registration(self, registration):
        self.registration = registration

    def get_origin_car(self):
        return self.origin_car

    def set_origin_car(self, origin_car):
        self.origin_car = origin_car

    def get_document(self):
        return self.document

    def set_document(self, document):
        self.document = document
