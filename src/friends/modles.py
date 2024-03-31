from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeMeta, declarative_base
from src.auth.models import user

Base: DeclarativeMeta = declarative_base()
metadata_friends = MetaData()

friend = Table(
    "friend",
    metadata_friends,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("user_id", Integer, ForeignKey(user.c.id), nullable=False),
    Column("friend_id", Integer, ForeignKey(user.c.id), nullable=False),
)


class FriendTable(Base):
    __tablename__ = "friend"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
    friend_id = Column(Integer, ForeignKey(user.c.id), nullable=False)
