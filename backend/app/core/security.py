from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
import jwt

from app.core.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    """Hash a password using pwdlib."""
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash using pwdlib."""
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(user_id: int) -> str:
    """Create a JWT access token for a given user ID."""
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {
        "sub": str(user_id),
        "exp": expire
    }
    token = jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return token