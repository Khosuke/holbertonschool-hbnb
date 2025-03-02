"""
This modules defines the Review subclass
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    This class contains everything about a
    Review made by a User about a place.

    Attributes:
        - text (String): The content of the review.
            Required.
        - rating (Integer): Rating given to the place.
            Must be between 1 and 5.
        - place (String): Place ID being reviewed.
            Must be validated to ensure the place exists.
        - user (String): User ID of who wrote the review.
            Must be validated to ensure the user exists.
    """
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text    
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise TypeError("Text must be a string")
        self._text = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("Rating must be an integer number")
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between a number between 1 and 5")
        self._rating = value

    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Place ID must be a string")
        self._place_id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, str):
            raise ValueError("User ID must be a string")
        self._user_id = value

    def to_dict(self):
        """
        return a dictionary
        """
        return {'id': self.id, 'text': self.text,\
                    'rating': self.rating, 'user_id': self.user_id, 'place_id': self.place_id}
