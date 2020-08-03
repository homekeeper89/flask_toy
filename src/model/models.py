from src.database import db
from sqlalchemy.sql import func
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __table_name__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=True)
    age = db.Column(db.Integer)

    # todos.author를 하면 user_id가 나온다..?

    def to_entity(self):
        return {"id": self.id, "email": self.email}

    @classmethod
    def create(cls, **kwards):
        obj = cls(**kwards)
        db.session.add(obj)
        db.session.commit()

    @classmethod
    def get_user(cls, id: int):
        return db.session.query(User).filter(User.id == id).first()


class Todos(db.Model):
    __table_name__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    contents = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref="todos", lazy=True)  # 객체 이름을 받는다.
    # 가상의 필드이고 연결된 객체(여기선 "User")에서 author로 불러올 수 있따.
