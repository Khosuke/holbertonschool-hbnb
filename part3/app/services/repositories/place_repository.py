from app.persistence.repository import SQLAlchemyRepository
from app.models.amenity import Amenity
from app import db

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self, model):
        super().__init__(model)

    def add_amenities(self, place, amenities):
        for amenity_id in amenities:
            amenity = db.session.get(Amenity, amenity_id)
            if not amenity:
                raise KeyError('Invalid input data')
            else:
                place.amenities.append(amenity)
        db.session.add(place)
        db.session.commit()
        
    def get(self, place_id):
        return db.session.query(self.model).filter_by(id=place_id).first()
