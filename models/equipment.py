
class Equipment:
    def __init__(self, name=None, type=None, features=None):
        self.name = name
        self.type = type
        self.features = features

    def __str__(self):
        return f"Equipment(name='{self.name}', type='{self.type}', features='{self.features}')"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_features(self):
        return self.features

    def set_features(self, features):
        self.features = features
