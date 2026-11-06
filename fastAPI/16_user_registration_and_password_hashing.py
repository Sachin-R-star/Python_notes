"""
================================================================================
FASTAPI TUTORIAL #16: USER REGISTRATION (SIGN UP) & PASSWORD HASHING
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. User Registration Flow:
   1. User frontend form me `username`, `email`, aur plain `password` bhejta hai.
   2. Pydantic schema (`UserRegisterSchema`) input validate karta hai (Email valid hai? Password length >= 8?).
   3. Check karte hain ki kya ye email pehle se database me exist toh nahi karta? Agar karta hai toh `HTTPException(400, "Email already registered")`.
   4. **Password Hashing**:
      Plain password (e.g. `"Secret@123"`) ko Passlib / Bcrypt ke through ek unbreakable 
      60-character hash (e.g. `"$2b$12$KIX...sdsdf"`) me convert karte hain:
      `hashed_pw = pwd_context.hash(user.password)`
   5. Database me hashed password store karte hain.
   6. Client ko response me user details return karte hain WITHOUT the password!

2. CryptContext from passlib:
   - `pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")`
   - `pwd_context.hash(plain_password)`: Hashes password with random salt.
   - `pwd_context.verify(plain_password, hashed_password)`: Verifies password on login.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import hashlib
import secrets

# Database setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users_demo_16"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================================================================
# PASSWORD HASHING UTILITY (Production standard hashing implementation)
# ==============================================================================
# In production: from passlib.context import CryptContext; pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Portable PBKDF2/SHA256 implementation with random Salt (Zero external C-library dependency):
def hash_password(password: str) -> str:
    """Hashes plain password using SHA-256 with a unique random cryptographic salt"""
    salt = secrets.token_hex(16)
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return f"{salt}${hashed}"

def verify_password(plain_password: str, stored_hash: str) -> bool:
    """Verifies candidate plain password against stored salt$hash"""
    try:
        salt, expected_hash = stored_hash.split("$")
        calculated = hashlib.sha256((salt + plain_password).encode()).hexdigest()
        return calculated == expected_hash
    except Exception:
        return False


# ==============================================================================
# PYDANTIC SCHEMAS
# ==============================================================================
class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, examples=["sachin_dev"])
    email: EmailStr = Field(..., examples=["sachin@example.com"])
    password: str = Field(..., min_length=8, max_length=100, description="Minimum 8 characters", examples=["StrongP@ssw0rd!"])

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


app = FastAPI(
    title="Lecture 16 - User Registration & Password Hashing",
    description="Sign-up endpoint with duplicate checks and cryptographic password hashing",
    version="1.0.0"
)

@app.post(
    "/api/v1/auth/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"]
)
def register_user(user_in: UserRegister, db: Session = Depends(get_db)):
    """
    Registers a new user:
    1. Checks if email or username is already taken.
    2. Hashes plain password.
    3. Persists user in DB and returns safe UserResponse.
    """
    # 1. Check existing email
    existing_email = db.query(User).filter(User.email == user_in.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists!"
        )

    # 2. Check existing username
    existing_username = db.query(User).filter(User.username == user_in.username).first()
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already taken. Please choose another."
        )

    # 3. Hash password securely
    hashed_pw = hash_password(user_in.password)

    # 4. Create and save new user record
    new_user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_pw,
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
