from flask import Blueprint, jsonify, Response

from project import db
from project.api.models import User


user_blueprint = Blueprint(
    "users",
    __name__
)


@user_blueprint.route("/api/users")
def get_users():
    response = []
    users = db.session.query(User).all()
    for user in users:
        response.append(user.to_dict())
    return jsonify(response)


@user_blueprint.route("/api/users/<int:user_id>")
def get_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return Response(status=404)
    return jsonify(user.to_dict())
