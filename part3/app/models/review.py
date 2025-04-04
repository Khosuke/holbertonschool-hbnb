from .baseclass import BaseModel
from .place import Place
from .user import User
from app import db

class Review(BaseModel):
	__tablename__ = "review"

	_text = db.Column(db.String(100), nullable=False)
	_rating = db.Column(db.Integer, nullable=False)
	_place = db.Column(db.String(36), db.ForeignKey('place.id', ondelete="CASCADE"), nullable=False)
	_user = db.Column(db.String(36), db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)


	@property
	def text(self):
		return self._text
	
	@text.setter
	def text(self, value):
		if not value:
			raise ValueError("Text cannot be empty")
		if not isinstance(value, str):
			raise TypeError("Text must be a string")
		self._text = value

	@property
	def rating(self):
		return self._rating
	
	@rating.setter
	def rating(self, value):
		if not isinstance(value, int):
			raise TypeError("Rating must be an integer")
		super().is_between('Rating', value, 1, 6)
		self._rating = value

	@property
	def place(self):
		return self._place
	
	@place.setter
	def place(self, value):
		if not isinstance(value, Place):
			raise TypeError("Place must be a place instance")
		self._place = value

	@property
	def user(self):
		return self._user
	
	@user.setter
	def user(self, value):
		if not isinstance(value, User):
			raise TypeError("User must be a user instance")
		self._user = value

	def to_dict(self):
		return {
			'id': self.id,
			'text': self._text,
			'rating': self._rating,
			'place_id': self._place,
			'user_id': self._user
		}
