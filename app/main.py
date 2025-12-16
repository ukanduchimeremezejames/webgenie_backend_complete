
from fastapi import FastAPI
from app.api.routes import datasets, algorithms

app = FastAPI(title="BEELINE Benchmarking API")

app.include_router(datasets.router, prefix="/datasets", tags=["datasets"])
app.include_router(algorithms.router, prefix="/algorithms", tags=["algorithms"])
