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

    # User Methods
    def create_user(self, user_data):
        """Create a new user and store in memory."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user
    
    def get_all_users(self):
        """Get a list of all users."""
        users = self.user_repo.get_all()
        return [user.to_dict() for user in users]

    def get_user(self, user_id):
        """Get user by ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Fetch user by email."""
        return self.user_repo.get_by_attribute('email', email)
    
    def update_user(self, user_id, user_data):
        """Update existing user."""
        self.user_repo.update(user_id, user_data)
        return self.user_repo.get(user_id)

    # Amenity Methods
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        amenities = self.amenity_repo.get_all()
        return [amenity.to_dict() for amenity in amenities]

    def update_amenity(self, amenity_id, amenity_data):
        self.amenity_repo.update(amenity_id, amenity_data)
        return self.amenity_repo.get(amenity_id)

    # Place Methods
    def create_place(self, place_data):
        """Create a new place."""
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        """Get place by ID."""
        return self.place_repo.get(place_id)

    def get_all_places(self):
        """Get all places."""
        places = self.place_repo.get_all()
        return [place.to_dict() for place in places]

    def update_place(self, place_id, place_data):
        """Update an existing place."""
        self.place_repo.update(place_id, place_data)
        return self.place_repo.get(place_id)

    # Review Methods
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        reviews = self.review_repo.get_all()
        return [review.to_dict() for review in reviews]

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        return place.reviews if place else []

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)
