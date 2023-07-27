from flask_restx import Namespace
from flask_restx import Resource

from app.models.user import User

user_np = Namespace("user", description="user views for test only")


@user_np.route("/user")
class UserBaseEndpoint(Resource):
    def get(self):
        ret = []
        res = User.query.all()
        for user in res:
            ret.append({"username": user.username, "email": user.email})
        return ret, 200
