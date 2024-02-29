from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData, Column, Integer, String, Text


metadata = MetaData()

Base = declarative_base(metadata=metadata)


class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)


class Establishment(Base):
    __tablename__ = "establishment"

    establishment_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String, nullable=False)
    opening_hours = Column(String, nullable=False)
