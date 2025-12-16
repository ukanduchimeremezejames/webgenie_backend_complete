
from pydantic import BaseModel

class DatasetOut(BaseModel):
    dataset_id: str
    name: str
    organism: str

    class Config:
        orm_mode = True
