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
        - place (Place): Place instance being reviewed.
            Must be validated to ensure the place exists.
        - user (User): User instance of who wrote the review.
            Must be validated to ensure the user exists.
    """
    def __init__(self, text, rating, place, user):


        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
