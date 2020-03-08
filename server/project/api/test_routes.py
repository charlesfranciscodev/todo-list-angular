from flask import Blueprint, jsonify


test_blueprint = Blueprint(
    "test",
    __name__
)


@test_blueprint.route("/api/test")
def test():
    response = {
        "message": "Yo mamma so fat even penguins are jealous of the way she waddles."
    }
    return jsonify(response)
