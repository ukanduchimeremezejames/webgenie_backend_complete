
from pydantic import BaseModel

class AlgorithmOut(BaseModel):
    algorithm_id: str
    name: str

    class Config:
        orm_mode = True
