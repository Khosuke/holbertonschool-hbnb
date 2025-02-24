#!/usr/bin/python3
"""
create a user class
"""

from app.models.base_model import BaseModel

class User(BaseModel):
    """
    create a new_user
    """

    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        initialize inscription new user
        """
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("The first name and last name must be strings")
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError(
                " First name and Last name must be less than 50 characters")

        super().__init__()

        self.first_name = first_name
        self.last_name = last_name
        self.__email = email
        # self.__password = password
        self.__is_admin = is_admin
        self.reviews = []
        self.places = []

    @property
    def email(self):
        """
        return email of user
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        defined a new email
        """
        self.__email = value

    """
    @property
    def password(self):

        Return a password (hidden)

        return

    @password.setter
    def password(self, value):

        Define a new password

        if len(value) < 6:
            raise ValueError("the password must be have minimum six character")
            self.__password = value
    """
    @property
    def is_admin(self):
        """
        verify if the user is an admin
        """
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        """
        Define the admin role
        """
        if not isinstance(value, bool):
            raise ValueError("is_admin must be boolean")
        self.__is_admin = value

    def add_review(self, review):
        """
        add one review by the user
        """
        self.reviews.append(review)

    def add_place(self, place):
        """
        add new place by user
        """
        self.places.append(place)
