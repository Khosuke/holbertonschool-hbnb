#!/usr/bin/python3
"""
for admin
"""


from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('admin', description='Admin operations')

@api.route('/users/<user_id>')
class AdminUserResource(Resource):
    @jwt_required()
    def put(self, user_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)

        # If 'is_admin' is part of the identity payload
        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        if email:
            # Check if email is already in use
            existing_user = facade.get_user_by_email(email)
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        try:
            facade.update_user(user_id, user_data)
            return user.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400


@api.route('/users/')
class AdminUserCreate(Resource):
    @jwt_required()
    def post(self):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)
        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
            return new_user.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400



@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    def post(self):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)
        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        amenity_data = api.payload
        
        existing_amenity = facade.amenity_repo.get_by_attribute('name', amenity_data.get('name'))
        if existing_amenity:
            return {'error': 'Invalid input data'}, 400
        try:
            new_amenity = facade.create_amenity(amenity_data)
            return new_amenity.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400


@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    def put(self, amenity_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)
        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        amenity_data = api.payload
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        try:
            facade.update_amenity(amenity_id, amenity_data)
            return {"message": "Amenity updated successfully"}, 200
        except Exception as e:
            return {'error': str(e)}, 400


@api.route('/places/<place_id>')
class AdminPlaceDelete(Resource):
    @jwt_required()
    def delete(self, place_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)

        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        place_data = api.payload
        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404

        try:
            facade.update_place(place_id, place_data)
            return {'message': 'Place updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400

@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)

        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        try:
            facade.delete_place(place_id)
            return {'message': 'Place deleted successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400

@api.route('/reviews/<review_id>')
class AdminReviewModify(Resource):
    @jwt_required()
    def put(self, review_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)

        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        review_data = api.payload
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        try:
            facade.update_review(review_id, review_data)
            return {'message': 'Review updated successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400

@api.route('/places/<place_id>')
class AdminDeleteReview(Resource):
    @jwt_required()
    def delete(self, review_id):
        get_token = get_jwt()
        is_admin = get_token.get('is_admin', False)

        if not is_admin:
            return {'error': 'Admin privileges required'}, 403

        review_data = api.payload
        review = facade.get_review(review_id)

        if not review:
            return {'error': 'Review not found'}, 404

        try:
            facade.delete_review(review_id, review_data)
            return {'message': 'Review deleted successfully'}, 200
        except Exception as e:
            return {'error': str(e)}, 400
