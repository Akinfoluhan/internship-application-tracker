from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import text
from app.api.routes.applications import router as applications_router
from app.api.routes.auth import router as auth_router

app = FastAPI()

app.include_router(applications_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-health")
def db_health_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT current_database();"))
    return {"database": result.scalar_one()}
