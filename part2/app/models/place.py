from .base_model import BaseModel



class Place(BaseModel):

    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities):
        if not isinstance(title, str):
            raise TypeError('Title must be a string')
        if len(title) > 100:
            raise ValueError('Title maximum length is 100 characters')
        if not isinstance(description, str):
            raise TypeError('Description must be a string')
        if not isinstance(price, (float, int)):
            raise TypeError('Price must be an integer or decimal number')
        if price < 0:
            raise ValueError('Price must be positive')
        if not isinstance(latitude, (float, int)):
            raise TypeError('Latitude must be an integer or decimal number')
        if not isinstance(longitude, (float, int)):
            raise TypeError('Longitude must be an integer or decimal number')
        if not -90 <= latitude <= 90:
            raise ValueError('Latitude must be in between -90 and 90')
        if not -180 <= longitude <= 180:
            raise ValueError('Longitude must be in between -180 and 180')
        if not isinstance(owner_id, str):
            raise TypeError('Owner ID must be a valid ID string')
        if not isinstance(amenities, list):
            raise TypeError('Amenities must be a list of a amenities ID')
        if not all(isinstance(amenity_id, str) for amenity_id in amenities):
            raise ValueError('Amenities list element must all be strings')
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities
        self.reviews = []

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
        from app.services import facade
        return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'price': self.price,
                'latitude': self.latitude,
                'longitude': self.longitude,
                'owner_id': self.owner_id,
                'amenities': [(facade.get_amenity(amenity).to_dict()) for amenity in self.amenities]
                }, 201
