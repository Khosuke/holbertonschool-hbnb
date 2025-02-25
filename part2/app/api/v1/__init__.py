#!/usr/bin/python3


from flask_restx import Api
from .users import api as users_ns

api = Api(
    title="My API",
    version="1.0",
    description="A simple API",
)

api.add_namespace(users_ns, path="/users")