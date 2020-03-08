import json

from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Todo, User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command("recreate_db")
def recreate_db():
    """Delete all the data in the database and recreate all tables."""
    db.reflect()
    db.drop_all()
    db.create_all()
    db.session.commit()


def create_users():
    with open("users.json") as f:
        users = json.load(f)
        for user_dict in users:
            user = User()
            user.first_name = user_dict["firstName"]
            user.last_name = user_dict["lastName"]
            user.username = user_dict["username"]
            user.avatar_url = user_dict["avatarUrl"]
            db.session.add(user)
    db.session.commit()


def create_todos():
    with open("todos.json") as f:
        todos = json.load(f)
        for todo_dict in todos:
            todo = Todo()
            todo.title = todo_dict["title"]
            todo.content = todo_dict["content"]
            todo.completed = todo_dict["completed"]
            todo.due_date = todo_dict["dueDate"]
            todo.priority = todo_dict["priority"]
            user = User.query.filter_by(username=todo_dict["username"]).first()
            todo.user_id = user.user_id
            db.session.add(todo)
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    """Seeds the database."""
    print("Creating Users")
    create_users()
    print("Creating Todos")
    create_todos()
    print("Done")


if __name__ == "__main__":
    cli()
