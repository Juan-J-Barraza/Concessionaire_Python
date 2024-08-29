

class Client:
   def __init__(self, name, last_name, doc_type, doc_number, seller):
    self.name = name
    self.last_name = last_name
    self.doc_type = doc_type
    self.doc_number = doc_number
    self.seller = seller

    
    def __str__(self):
        return f"Client(name={self.name}, last_name={self.last_name}, document_type={self.document_type}, document_number={self.document_number})"
    
    def get_name(self):
        return self.name
    
    def set_name(self,  name):
        self.name = name

    def get_last_name(self):
        return self.last_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def get_type_document(self):
        return self.type_document
    
    def set_type_document(self, type_document):
        self.type_document = type_document

    def get_number_document(self):
        return self.number_document
    
    def set_number_document(self, number_document):
        self.number_document = number_document
    
    def get_seller(self):
        return self.seller
    
    def set_seller(self, seller):
        self.seller = seller