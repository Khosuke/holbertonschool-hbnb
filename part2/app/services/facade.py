from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

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
    
    def get_all_users(self):
        """
        get a list of all users
        """
        list = self.user_repo.get_all()
        user_list = [user.to_dict() for user in list]
        return user_list

    def get_user(self, user_id):
        """
        get user by ID
        return user if exist else leave error
        """
        user = self.user_repo.get(user_id)
        return user

    def get_user_by_email(self, email):
        """
        Fetch user by email 
        """
        return self.user_repo.get_by_attribute('email', email)
    

    def update_user(self, user_id, user_data):
        """
        update existing users
        """
        self.user_repo.update(user_id, user_data)
        updated_user = self.user_repo.get(user_id)
        return updated_user

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return {"error": "Amenity not found"}, 404
        return amenity

    def get_all_amenities(self):
        list = self.amenity_repo.get_all()
        amenity_list = [amenity.to_dict() for amenity in list]
        return amenity_list

    def update_amenity(self, amenity_id, amenity_data):
            self.amenity_repo.update(amenity_id, amenity_data)
            updated_amenity = self.amenity_repo.get(amenity_id)
            return updated_amenity

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
            return {"error": "Place not found"}, 404
        return place

    def get_all_places(self):
        """
        get all places
        """
        list = self.place_repo.get_all()
        place_list = [place.to_dict() for place in list]
        return place_list

    def update_place(self, place_id, place_data):
        """
        update existing  places
        """
        self.place_repo.update(place_id, place_data)
        updated_place = self.place_repo.get(place_id)
        return updated_place

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review.to_dict()

    def get_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return review.to_dict()

    def get_all_reviews(self):
        list = self.review_repo.get_all()
        review_list = [review.to_dict() for review in list]
        return review_list

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        return place["reviews"]

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        updated_review = self.review_repo.get(review_id)
        return updated_review.to_dict()

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
