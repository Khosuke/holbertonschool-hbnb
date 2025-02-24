#!/usr/bin/python3
"""
create a user class
"""

from base_model import BaseModel

class User(BaseModel):
    """
    create a new_user
    """


    def __init__(self, name, last_name, email, password, is_admin=False):
        """
        initialize inscription new user
        """

        super().__init__()

        self.name = name
        self.last_name = last_name
        self.__email = email
        self.__password = password
        self.__is_admin = is_admin

        
        
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
        if "@" not in value:
            raise ValueError("Email be must contain '@'")
            self.__email = value


    @property
    def password(self):
        """
        Return a password (hidden)
        """
        return "****************"
        
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
        verify is the user is a admin
        """
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        """
        Define the admin status
        """
        if not isinstance(value, bool):
            raise ValueError("is_admin must be boolean")
            self.__is_admin = value
