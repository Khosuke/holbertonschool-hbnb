from app.persistence.repository import InMemoryRepository
from app.models.user import User
import uuid
from flask_restx import abort

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """
        create a new user and store in memory
        """
        existing_user = self.get_user_by_email(user_data['email'])
        if existing_user:
            abort(400, message="Email already registered")

        user_id = str(uuid.uuid4())
        user = User(id=user_id, **user_data)
        self.user_repo.add(user)
        return user 

    def get_user_by_email(self, email):
        """
        Fetch user by email 
        """
        return self.user_repo.get_by_attribute('email', email)
    
    def get_place(self, place_id):

        pass

    def get_user(self, user_id):
        """
        get user by ID
        return user if exist else leave error
        """
        user = self.user_repo.get(user_id)
        if not user:
            abort(404, message="User not found")
        return user

    def put_user(self, user_id, user):
        """
        update existing users and
        verify without deleted another existing value
        """
        existing_user = self.get_user(user_id)
        if not existing_user:
            abort(404, message="User not found")
        
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }

        if 'email' in user_data:
            existing_user_by_email = self.get_user_by_email(user_data['email'])
            if existing_user_by_email and existing_user_by_email.id != user_id:
                abort(400, message="Email is already registered with another user")
        try:
            self.user_repo.update(existing_user.id, user_data)
        except Exception as e:
            abort(500, message=f"Error updating user: {e}")

