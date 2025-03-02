from .base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    Args:
        -name (String): The name of the amenity (e.g., "Wi-Fi", "Parking").
        Required, maximum length of 50 characters.
        -place (list): List of places associated with the amenity.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.place = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if not value or len(value) > 50:
            raise ValueError("The name of the amenity must not exceed 50 characters.")
        self._name = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        if not isinstance(value, list):
            raise TypeError("Place must be a list")
        self._place = value

    def add_place(self, place):
        """
        method that add a place to an amenity
        Args:
            -place (Place): The place to add.
        """
        self.place.append(place)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}
