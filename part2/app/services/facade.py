from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.review import Review
from app.models.place import Place
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user


    def get_user(self, user_id):
        return self.user_repo.get(user_id)


    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        updated_user = self.user_repo.update(user_id, user_data)
        return updated_user

    def get_place(self, place_id):
        return self.user_repo.get(place_id)


    def create_place(self, place_data):
    # Placeholder for logic to create a place, including validation for price, latitude, and longitude
        pass


    def get_place(self, place_id):
        return self.place_repo.get(place_id)


    def get_all_places(self):
        list = self.place_repo.get_all()
        place_list = (place.to_dict() for place in list)
        return place_list

    def update_place(self, place_id, place_data):
    # Placeholder for logic to update a place
        pass

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        return place["reviews"]

    def update_review(self, review_id, review_data):
        self.review_repo.update(review_id, review_data)
        updated_review = self.review_repo.get(review_id)
        return updated_review

    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)


    def put_user(self, user_id, user_data):
        """
        update existing users and
        verify without deleted another existing value
        """
        existing_user = self.get_user(user_id)
        if not existing_user:
            return {"error": "User not found"}, 404

        if 'email' in user_data:
            existing_user_by_email = self.get_user_by_email(user_data['email'])
            if existing_user_by_email and existing_user_by_email.id != user_id:
                return {"error": "Email is already registered with another user"}, 400
        try:
            self.user_repo.update(existing_user.id, user_data)
        except Exception as e:
            return {"error":  str(e)}, 400
