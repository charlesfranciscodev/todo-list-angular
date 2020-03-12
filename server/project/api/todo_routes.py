from flask import Blueprint, jsonify, request, Response

from project import db
from project.api.models import Todo, User


todo_blueprint = Blueprint(
    "todos",
    __name__
)


@todo_blueprint.route("/api/todos")
def get_todos():
    response = []
    todos = db.session.query(Todo).all()
    for todo in todos:
        response.append(todo.to_dict())
    return jsonify(response)


@todo_blueprint.route("/api/todos/<int:todo_id>")
def get_todo(todo_id):
    todo = Todo.query.filter_by(todo_id=todo_id).first()
    if not todo:
        return Response(status=404)
    return jsonify(todo.to_dict())


@todo_blueprint.route("/api/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = Todo.query.filter_by(todo_id=todo_id).first()
    if not todo:
        return Response(status=404)
    db.session.delete(todo)
    db.session.commit()
    return Response(status=204)


@todo_blueprint.route("/api/todos", methods=["POST", "PUT"])
def create_or_update_todo():
    response = {}
    request_json = request.get_json()

    import sys
    print("request data...", request_json, file=sys.stderr)

    # Validation
    keys = ["title", "content", "completed", "dueDate", "priority"]
    if request.method == "PUT":
        keys.append("todoId")
    for key in keys:
        if key not in request_json:
            response["message"] = "Missing {key} in request body".format(key=key)
            return jsonify(response), 400

    user_id = request_json.get("userId")
    if user_id:
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            response["message"] = "User not found"
            return jsonify(response), 404

    # Parse the request data
    todo = None
    if request.method == "POST":
        todo = Todo()
    elif request.method == "PUT":
        todo_id = int(request_json["todoId"])
        todo = Todo.query.filter_by(todo_id=todo_id).first()
        if not todo:
            response["message"] = "Todo not found"
            return jsonify(response), 404

    todo.title = request_json["title"]
    todo.content = request_json["content"]
    todo.completed = request_json["completed"]
    todo.due_date = request_json["dueDate"]
    todo.priority = request_json["priority"]
    if "userId" in request_json:
        todo.user_id = user_id

    if request.method == "POST":
        db.session.add(todo)
        response["message"] = "Todo created successfully"
    elif request.method == "PUT":
        response["message"] = "Todo updated successfully"
    db.session.commit()
    response["todoId"] = todo.todo_id
    
    return jsonify(response), 201
