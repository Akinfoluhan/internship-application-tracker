from app.core.database import SessionLocal
from sqlalchemy import text

with SessionLocal() as session:
    result = session.execute(text("SELECT current_database();"))
    print(result.scalar_one())