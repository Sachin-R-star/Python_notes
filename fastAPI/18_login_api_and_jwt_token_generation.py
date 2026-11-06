"""
================================================================================
FASTAPI TUTORIAL #18: LOGIN API & JWT TOKEN GENERATION
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Login API Architecture:
   1. User apna username/email aur password bhejta hai.
   2. Backend database me user record find karta hai:
      `user = db.query(User).filter(User.email == credentials.email).first()`
   3. Agar user nahi mila, ya password match nahi hua (`not verify_password(...)`):
      * ATTACK PREVENTION NOTE: Kabhi specific error mat do ki "Password galat hai" ya "Email galat hai".
      * Hamesha generic error do: `401 Unauthorized: "Invalid email or password"`.
        (Taaki hacker ko pata na chale ki kaunsi email system me exist karti hai!).
   4. Jab credentials verify ho jayein, toh hum ek **JWT Access Token** generate karte hain:
      `token = create_access_token(data={"sub": user.email, "user_id": user.id})`
   5. Standard OAuth2 Response format me token return karte hain:
      `{"access_token": token, "token_type": "bearer"}`

2. Bearer Token kya hota hai?
   - "Bearer" ka matlab hota hai "jiske paas yeh token hai, wahi owner hai".
   - Iske baad client har protected API request ke header me ye token bhejega:
     `Authorization: Bearer <your_jwt_token>`
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, timedelta
import jwt
import hashlib
import secrets

# JWT Security Configurations
SECRET_KEY = "my_ultra_secure_jwt_secret_key_change_in_production_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 Hour

# Mock User Database with Pre-hashed passwords
def make_hash(pw: str) -> str:
    salt = "fixed_salt_for_demo"
    return f"{salt}${hashlib.sha256((salt + pw).encode()).hexdigest()}"

def check_pw(plain: str, stored: str) -> bool:
    salt, expected = stored.split("$")
    return hashlib.sha256((salt + plain).encode()).hexdigest() == expected

USERS_DATABASE = {
    "sachin@dev.com": {
        "id": 101,
        "username": "sachin_dev",
        "email": "sachin@dev.com",
        "hashed_password": make_hash("PythonMaster@2026"),
        "role": "admin"
    }
}


# JWT Generation Function
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Creates encoded JWT token with expiry payload"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Pydantic Schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in_minutes: int


app = FastAPI(
    title="Lecture 18 - Login API & JWT Generation",
    description="Authenticating user credentials and generating signed JWT Bearer tokens",
    version="1.0.0"
)

@app.post(
    "/api/v1/auth/login",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
    tags=["Authentication"]
)
def login_for_access_token(credentials: LoginRequest):
    """
    Authenticate user and issue JWT Access Token.
    """
    # 1. Fetch user from DB
    user = USERS_DATABASE.get(credentials.email)

    # 2. Verify identity & password
    if not user or not check_pw(credentials.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password. Authentication failed.",
            headers={"WWW-Authenticate": "Bearer"}
        )

    # 3. Create Access Token with payload claims (sub = subject / user identifier)
    token_data = {
        "sub": user["email"],
        "user_id": user["id"],
        "role": user["role"]
    }
    jwt_token = create_access_token(token_data)

    # 4. Return standard OAuth2 token response
    return {
        "access_token": jwt_token,
        "token_type": "bearer",
        "expires_in_minutes": ACCESS_TOKEN_EXPIRE_MINUTES
    }
