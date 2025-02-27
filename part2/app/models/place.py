from .base_model import BaseModel



class Place(BaseModel):

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = []
        self.amenities = amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def to_dict(self):
        """
        return a dictionary
        """
        return {'id': self.id, 'title': self.title, 'description': self.description,\
                'price': self.price, 'latitude': self.latitude,\
                    'longitude': self.longitude, 'owner_id': self.owner_id}