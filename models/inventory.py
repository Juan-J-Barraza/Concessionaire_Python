
class Inventory:
    def __init__(self, concessionaire=None):
        self.concessionaire = concessionaire
     

    def __str__(self):
        return f"Inventory(concessionaire={self.concessionaire})"

    def get_location(self):
        return self.concessionaire

    def set_concessionaire(self, concessionaire):
        self.concessionaire = concessionaire
