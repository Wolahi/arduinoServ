from sqlalchemy import MetaData, Table, Column, Integer, Text
from sqlalchemy.orm import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()
metadata_temp = MetaData()

temp = Table(
    "temperature",
    metadata_temp,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=True),
    Column("temp_value", Integer, nullable=False),
    Column("date", Text, nullable=False),
)


class TempTable(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    temp_value = Column(Integer, nullable=False)
    date = Column(Text, nullable=False)
