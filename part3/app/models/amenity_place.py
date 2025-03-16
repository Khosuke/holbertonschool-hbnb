from app import db


amenity_place = db.Table('amenity_place',
    db.Column('place_id', db.String(36), db.ForeignKey('place.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenity.id'), primary_key=True)
)  
