from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ApplicationCreate(BaseModel):
    company: str | None = None
    role_title: str | None = None
    status: str | None = None

applications = []
next_id = 1

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/applications")
def get_applications():
    return applications

@app.post("/api/applications")
def create_application(application: ApplicationCreate):
    global next_id
    new_application = application.model_dump()
    new_application["id"] = next_id
    applications.append(new_application)
    next_id += 1
    return new_application

@app.get("/api/applications/{application_id}")
def get_application(application_id: int):
    for app in applications:
        if app["id"] == application_id:
            return app
    raise HTTPException(status_code=404, detail="Application not found")

@app.patch("/api/applications/{application_id}")
def update_application(application_id: int, application: ApplicationCreate):
    for app in applications:
        if app["id"] == application_id:
            app.update(application.model_dump(exclude_unset=True))
            return app
    raise HTTPException(status_code=404, detail="Application not found")

@app.delete("/api/applications/{application_id}")
def delete_application(application_id: int):
    for app in applications:
        if app["id"] == application_id:
            applications.remove(app)
            return {"detail": "Application deleted"}
    raise HTTPException(status_code=404, detail="Application not found")