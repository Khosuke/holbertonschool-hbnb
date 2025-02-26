from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
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
        user = User(**user_data)
        self.user_repo.add(user)
        return user 

    def get_user(self, user_id):
        """
        get user by ID
        return user if exist else leave error
        """
        user = self.user_repo.get(user_id)
        if not user:
            abort(404, message="User not found")
        return user

    def get_user_by_email(self, email):
        """
        Fetch user by email 
        """
        return self.user_repo.get_by_attribute('email', email)
    

    def put_user(self, user_id, user):
        """
        update existing users and
        verify without deleted another existing value
        """
        existing_user = self.get_user(user_id)
        if not existing_user:
           return {"Error": str(e)}, 404
        
        user_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }

        if 'email' in user_data:
            existing_user_by_email = self.get_user_by_email(user_data['email'])
            if existing_user_by_email and existing_user_by_email.id != user_id:
                return {"Error": str(e)}, 400
        try:
            self.user_repo.update(existing_user.id, user_data)
        except Exception as e:
            return {"Error": str(e)}, 400

    def create_place(self, place_data):
        """
        create place
        """
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """
        get place by ID
        """
        place = self.place_repo.get(place_id)
        if not place:
            abort(404, message="Place not found")
        return place

    def get_all_places(self):
    # Placeholder for logic to retrieve all places
        pass

    def update_place(self, place_id, place_data):
        """
        updating places
        """
      
