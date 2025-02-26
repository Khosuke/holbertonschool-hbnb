"""Module that defines the Amenity class."""

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
        if not name or len(name) > 50:
            raise ValueError(
                "The name of the amenity must be provided\
                    and must not exceed 50 characters.")
        self.name = name
        self.place = []

    def add_place(self, place):
        """
        method that add a place to an amenity
        Args:
            -place (Place): The place to add.
        """
        self.place.append(place)
