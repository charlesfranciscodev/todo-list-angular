from project import db


class Todo(db.Model):
    __tablename__ = "todos"
    todo_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def to_dict(self):
        user = self.user.to_dict() if self.user else None
        return {
            "todoId": self.todo_id,
            "title": self.title,
            "content": self.content,
            "completed": self.completed,
            "dueDate": self.due_date.isoformat(),
            "priority": self.priority,
            "user": user,
        }


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    avatar_url = db.Column(db.Text, nullable=False)
    todos = db.relationship("Todo", backref="user", lazy=True)

    def to_dict(self):
        return {
            "userId": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "avatarUrl": self.avatar_url,
        }
