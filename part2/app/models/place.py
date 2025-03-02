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
        self.amenities = amenities
        self.reviews = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError('Title must be a string')
        if len(value) > 100:
            raise ValueError('Title maximum length is 100 characters')
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('Description must be a string')
        self._description = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('Price must be an integer or decimal number')
        if value < 0:
            raise ValueError('Price must be positive')
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value) -> None:
        if not isinstance(value, (float, int)):
            raise TypeError('Latitude must be a number')
        if not -90 <= value <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError('Longitude must be a number')
        if not -180 <= value <= 180:
            raise ValueError('Longitude must be between -180 and 180')
        self._longitude = value

    @property
    def owner_id(self):
        return self._owner_id

    @owner_id.setter
    def owner_id(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise TypeError('Owner ID must be a non-empty string')
        self._owner_id = value

    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        if not isinstance(value, list):
            raise TypeError('Amenities must be a list')
        if not all(isinstance(amenity_id, str) for amenity_id in value):
            raise ValueError('All elements in amenities must be strings')
        self._amenities = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        if not isinstance(value, list):
            raise TypeError('Reviews must be a list')
        self._reviews = value


    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def delete_review(self, review):
        """
        Removes a review from the user
        """
        self.reviews.remove(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def delete_amenity(self, amenity):
        self.amenities.remove(amenity)

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
