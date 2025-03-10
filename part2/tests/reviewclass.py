import sys
import os

# Add the parent directory (hbnb/) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity

def test_review_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="azerty1234")
    amenity = Amenity(name="Wi-Fi")
    place = Place(title="Cozy Apartment", description="A nice place to stay", price=100, latitude=37.7749, longitude=-122.4194, owner_id=user.id, amenities=[amenity.id])
    review = Review(text="Nice place", rating=5, user_id=user.id, place_id=place.id)
    assert review.text == "Nice place"
    assert review.rating == 5
    assert review.user_id == user.id
    assert review.place_id == place.id
    print("Review creation test passed!")

test_review_creation()
