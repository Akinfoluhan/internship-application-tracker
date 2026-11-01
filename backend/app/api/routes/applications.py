from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.application import Application
from app.schemas.applications import ApplicationCreate, ApplicationUpdate

router = APIRouter(
    prefix="/api/applications",
    tags=["Applications"],
)

applications = []
next_id = 1

@router.get("")
def get_applications():
    return applications

@router.post("")
def create_application(application: ApplicationCreate):
    global next_id
    new_application = application.model_dump()
    new_application["id"] = next_id
    applications.append(new_application)
    next_id += 1
    return new_application

@router.get("/{application_id}")
def get_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            return application
    raise HTTPException(status_code=404, detail="Application not found")

@router.patch("/{application_id}")
def update_application(application_id: int, app: ApplicationUpdate):
    for application in applications:
        if application["id"] == application_id:
            application.update(app.model_dump(exclude_unset=True))
            return application
    raise HTTPException(status_code=404, detail="Application not found")

@router.delete("/{application_id}")
def delete_application(application_id: int):
    for application in applications:
        if application["id"] == application_id:
            applications.remove(application)
            return {"detail": "Application deleted"}
    raise HTTPException(status_code=404, detail="Application not found")
