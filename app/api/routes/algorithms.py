
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.algorithm import Algorithm
from app.schemas.algorithm import AlgorithmOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[AlgorithmOut])
def list_algorithms(db: Session = Depends(get_db)):
    return db.query(Algorithm).all()
