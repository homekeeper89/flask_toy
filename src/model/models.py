from src.database import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    todos = db.relationship("Todos", backref="user", lazy=True)

    def to_entity(self):
        return {"id": self.id, "email": self.email}


class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    contents = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

