from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, BigInteger

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author = Column(String(50))
    pages = Column(Integer)
    published = Column(Date)

    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>".format(
            self.title, self.author, self.pages, self.published
        )


class UserModel(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    nickname = Column(String(50))
    birthday = Column(String(50))
    created_at = Column("created_at", DateTime)
    updated_at = Column("updated_at", DateTime)


class AuthenticationModel(Base):
    __tablename__ = "authentications"

    user_id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    category = Column(String(10), primary_key=True)
    identification = Column(String(50))
    secret = Column(String(10))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
