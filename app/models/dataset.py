
from sqlalchemy import Column, String, Integer, Text
from app.models.base import Base

class Dataset(Base):
    __tablename__ = "datasets"
    dataset_id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(Text)
    organism = Column(String)
