from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    company: str
    role_title: str
    status: str = "Saved"

class ApplicationUpdate(BaseModel):
    company: str | None = None
    role_title: str | None = None
    status: str | None = None