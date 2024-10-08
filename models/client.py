

class Client:
    
    
    def __init__(self, name, last_name, doc_type, doc_number, seller):
        self.name = name
        self.last_name = last_name
        self.doc_type = doc_type
        self.doc_number = doc_number
        self.seller = seller

    
    def __str__(self):
        return f"Client(name={self.name}, last_name={self.last_name}, document_type={self.doc_type}, document_number={self.doc_number})"
    
    def get_name(self):
        return self.name
    
    def set_name(self,  name):
        self.name = name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_doc_type(self):
        return self.doc_type
    
    def set_doc_type(self, doc_type):
        self.doc_type = doc_type

    def get_doc_number(self):
        return self.doc_number
    
    def set_doc_number(self, doc_number):
        self.doc_number = doc_number
    
    def get_seller(self):
        return self.seller
    
    def set_seller(self, seller):
        self.seller = seller