from app.persistence.repository import InMemoryRepository
from app.models.user import User
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
        return user_data        

    def get_user_by_email(self, email):
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
            raise ValueError("User not found")
        return user

    def put_user(self, user_id, update_data):
        """
        update existing users and
        verify without deleted another existing value
        """
        user = self.user_repo.get(user_id)
        if not user:
            raise ValueError("User not found")

        user["first_name"] = update_data.get("first_name", user["first_name"])
        user["last_name"] = update_data.get("last_name", user["last_name"])
        user["email"] = update_data.get("email", user["email"])

        self.user_repo.update(user_id, user)
        return user
