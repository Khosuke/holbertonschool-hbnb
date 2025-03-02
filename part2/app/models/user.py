#!/usr/bin/python3
"""
create a user class
"""

from app.models.base_model import BaseModel
import re

class User(BaseModel):
    """
    create a new_user
    """

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        """
        initialize inscription new user
        """
        verify_email = self.validate_email(email)
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.__email = verify_email
        self.__password = password
        self.__is_admin = is_admin
        self.reviews = []
        self.places = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("The first name must be a string")
        if len(value) > 50:
            raise ValueError("First name must be less than 50 characters")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise TypeError("The last name must be a string")
        if len(value) > 50:
            raise ValueError("Last name must be less than 50 characters")
        self._last_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not self.validate_email(value):
            raise ValueError("Invalid email format")
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        self.__password = value

    @property
    def is_admin(self) -> bool:
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("is_admin must be a boolean")
        self.__is_admin = value


    def add_review(self, review):
        """
        add one review by the user
        """
        self.reviews.append(review)

    def delete_review(self, review):
        """
        removes a review from the user
        """
        self.reviews.remove(review)

    def add_place(self, place):
        """
        add new place by user
        """
        self.places.append(place)

    def delete_place(self, place):
        """
        removes a place from the user
        """
        self.reviews.remove(place)

    def to_dict(self):
        """
        Return a dictionary of the object
        """
        return {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
                }

    def validate_email(self, email):
        """
        Verify that the email is a valid format
        """
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(email_regex, email):
            return email
        raise ValueError("Email is not in a valid format")
