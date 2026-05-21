from fastapi import APIRouter, HTTPException
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
    for app in applications:
        if app["id"] == application_id:
            return app
    raise HTTPException(status_code=404, detail="Application not found")

@router.patch("/{application_id}")
def update_application(application_id: int, application: ApplicationUpdate):
    for app in applications:
        if app["id"] == application_id:
            app.update(application.model_dump(exclude_unset=True))
            return app
    raise HTTPException(status_code=404, detail="Application not found")

@router.delete("/{application_id}")
def delete_application(application_id: int):
    for app in applications:
        if app["id"] == application_id:
            applications.remove(app)
            return {"detail": "Application deleted"}
    raise HTTPException(status_code=404, detail="Application not found")
