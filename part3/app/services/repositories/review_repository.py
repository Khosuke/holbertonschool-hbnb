from app.models.review import Review
from app.persistence.repository import SQLAlchemyRepository
# from app import db

class ReviewRepository(SQLAlchemyRepository):
    def __init__(self, model):
        super().__init__(model)
