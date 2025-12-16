
from sqlalchemy import Column, String, Text
from app.models.base import Base

class Algorithm(Base):
    __tablename__ = "algorithms"
    algorithm_id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(Text)
