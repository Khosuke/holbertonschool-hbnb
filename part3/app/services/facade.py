from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository(User)
        self.amenity_repo = AmenityRepository(Amenity)
        self.place_repo = PlaceRepository(Place)
        self.review_repo = ReviewRepository(Review)

    # USER
    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user
    
    def get_users(self):
        return self.user_repo.get_all()

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)
    
    def update_user(self, user_id, user_data):
        self.user_repo.update(user_id, user_data)
    
    # AMENITY
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)

    # PLACE
    def create_place(self, place_data):        
        user = self.user_repo.get_by_attribute('id', place_data['_owner_id'])
        if not user:
            raise KeyError('Invalid input data')

        amenities = place_data.pop('amenities', [])
        place = Place(**place_data)
        self.place_repo.add(place)
        user.add_place(place)

        self.place_repo.add_amenities(place, amenities)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):

        return self.place_repo.update(place_id, place_data)

    # REVIEWS
    def create_review(self, review_data):
        user = self.user_repo.get(review_data['_user'])
        if not user:
            raise KeyError('Invalid input data')

        place = self.place_repo.get(review_data['_place'])
        if not place:
            raise KeyError('Invalid input data')

        review = Review(**review_data)
        self.review_repo.add(review)
        user.add_review(review)
        place.add_review(review)
        return review
        
    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        if not place:
            raise KeyError('Place not found')
        return place.reviews

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        
        user = self.user_repo.get(review._user)
        place = self.place_repo.get(review._place)

        user.delete_review(review)
        place.delete_review(review)
        self.review_repo.delete(review_id)
