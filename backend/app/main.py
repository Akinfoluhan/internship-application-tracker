from fastapi import FastAPI
from app.api.routes.applications import router as applications_router

app = FastAPI()

app.include_router(applications_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
