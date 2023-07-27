from flask import Blueprint
from flask_restx import Api

from .user import user_np

user_bp = Blueprint("user_bp", __name__)

api = Api(user_bp, title="Leasing api")

api.add_namespace(user_np, path="/user")
