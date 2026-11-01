from pydantic import BaseModel
from datetime import date

class ApplicationCreate(BaseModel):
    company: str
    role_title: str
    status: str = "Saved"
    location: str | None = None
    job_url: str | None = None
    source: str | None = None
    employment_type: str | None = None
    salary_range: str | None = None
    date_applied: date | None = None
    deadline: date | None = None
    description: str | None = None

class ApplicationUpdate(BaseModel):
    company: str | None = None
    role_title: str | None = None
    status: str | None = None
    location: str | None = None
    job_url: str | None = None
    source: str | None = None
    employment_type: str | None = None
    salary_range: str | None = None
    date_applied: date | None = None
    deadline: date | None = None
    description: str | None = None
