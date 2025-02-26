from flask_restx import Namespace, Resource, fields
from app.services import facade


api = Namespace('users', description='User operations')


user_model = api.model('User', {
    'first_name': fields.String(required=True, description="First name of the user"),
    'last_name': fields.String(required=True, description="Last name of the user"),
    'email': fields.String(required=True, description="Email of the user"),
    'password': fields.String(required=True, description="Password of the user")
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Error user')
    def post(self):
        """
        create a new user
        """
        user_data = api.payload

        if not all((user_data.get('first_name'), user_data.get('last_name'), user_data.get('email'), user_data.get('password'))):
            return {"error": "Missing required fields"}, 400

        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except Exception as e:
            print(f"Error creating user: {e}")
            return {"error": "User not created"}, 400

        return {
                'id': new_user.id,
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'email': new_user.email
                }, 201

@api.route('/<user_id>')
class UserResource(Resource):
    """
    Get by user ID
    """ 
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Get user by ID
        """
        try:
            user = facade.get_user(user_id)
        except Exception as e:
            print(f"Error retrieving user: {e}")
            return {"error": "An error occurred"}, 500

        if user is None:
            return {"error": "User not found"}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    def put(self, user_id):
        """
        Update already exist users
        """
        try:
            user = facade.get_user(user_id)
            if user is None:
                return {"error": "User not found"}, 404
        except Exception as e:
            print(f"Invalid input data: {e}")
            return {"error": "An error occurred"}, 500

        new_user_data = api.payload

        user.first_name = new_user_data.get('first_name')
        user.last_name = new_user_data.get('last_name')
        user.email = new_user_data.get('email')

        if 'password' in new_user_data:
            user.password = new_user_data['password']

        try:
            facade.put_user(user_id, user)
        except Exception as e:
            print(f"Error updating user: {e}")
            return {"error": "Internal server error"}, 500

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
