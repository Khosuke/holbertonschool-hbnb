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
        if not isinstance(text, str):
            raise TypeError("Text must be a string")
        if not isinstance(rating, int):
            raise TypeError("Rating must be an integer number")
        if 1 >= rating >= 5:
            raise ValueError("Rating must be between a number between 1 and 5")
        if not isinstance(place_id, str):
            raise ValueError("Place ID must be a string")
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string")
        super().__init__()
        self.text = text    
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
