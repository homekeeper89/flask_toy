from src.database import db
from sqlalchemy.sql import func


class User(db.Model):
    __table_name__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=True)

    # todos.author를 하면 user_id가 나온다..?

    def to_entity(self):
        return {"id": self.id, "email": self.email}


class Todos(db.Model):
    __table_name__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    contents = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    todo_user = db.relationship("User", backref="author", lazy=True)  # 객체 이름을 받는다.
    # author은 User에서 갖고 있는 속성. 페이지마다 설명이 다 다르네
