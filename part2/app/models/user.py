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
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("The first name and last name must be strings")
        if len(first_name) > 50 or len(last_name) > 50:
            raise ValueError("First name and Last name must be less than 50 characters")
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
        verify_email = self.validate_email(value)
        self.__email = verify_email

    
    @property
    def password(self):
        """
        Return a password (hidden)
        """
        return self.__password

    @password.setter
    def password(self, value):
        """
        Define a new password
        """
        if len(value) < 6:
            raise ValueError("the password must be have minimum six character")
        self.__password = value

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
