from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.application import Application
from app.schemas.applications import ApplicationCreate, ApplicationUpdate

router = APIRouter(
    prefix="/api/applications",
    tags=["Applications"],
)

@router.get("")
def get_applications(db: Session = Depends(get_db)):
    return db.execute(select(Application)).scalars().all()

@router.post("")
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    new_application = Application(**application.model_dump())
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    return new_application

@router.get("/{application_id}")
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.execute(select(Application).where(Application.id == application_id)).scalar_one_or_none()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

@router.patch("/{application_id}")
def update_application(application_id: int, app: ApplicationUpdate, db: Session = Depends(get_db)):
    application = db.execute(select(Application).where(Application.id == application_id)).scalars().first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    for key, value in app.model_dump(exclude_unset=True).items():
        setattr(application, key, value)
    db.commit()
    db.refresh(application)
    return application

@router.delete("/{application_id}")
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.execute(select(Application).where(Application.id == application_id)).scalars().first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
    return {"detail": "Application deleted"}
