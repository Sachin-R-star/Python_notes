"""
================================================================================
FASTAPI TUTORIAL #14: PRODUCTION-READY FASTAPI - BEST PRACTICES & SECURITY
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Production Ready API banane ke 4 Rules:
   
   - **Rule 1: Sensitive Data Leakage Prevention (response_model filter)**:
     Jab aap database se User fetch karte ho, toh user table me `hashed_password` aur 
     internal secrets bhi hote hain.
     Agar aap direct database model return kar doge, toh user ka password hash network par 
     leak ho jayega!
     Solution: Response Schema banao jisme `hashed_password` field hi na ho. FastAPI 
     automatically sensitive fields ko strip karke sirf allowed fields return karega!

   - **Rule 2: CORS Middleware (Cross-Origin Resource Sharing)**:
     React, Vue, ya Angular frontend agar kisi doosre domain/port (e.g. `localhost:3000`) par 
     chal raha hai aur backend `localhost:8000` par hai, toh browser security policy 
     (CORS Error) ki wajah se API request block kar deta hai.
     `CORSMiddleware` add karke hum specific frontend origins ko backend access allow karte hain.

   - **Rule 3: Global Exception Handlers**:
     Database down ho jaye ya code me koi unhandled bug aa jaye, toh raw Python Traceback 
     client ko nahi dikhna chahiye (Security vulnerability).
     Custom `@app.exception_handler` se hum uniform, clean JSON error responses return karte hain.

   - **Rule 4: API Versioning**:
     URLs me `/api/v1/...` use karo taaki jab v2 launch ho, toh puraani mobile apps crash na hon.
"""

from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

app = FastAPI(
    title="Lecture 14 - Production-Ready API Best Practices",
    description="CORS middleware, sensitive field filtering, and global exception handlers",
    version="1.0.0"
)

# ==============================================================================
# 1. CORS MIDDLEWARE CONFIGURATION
# ==============================================================================
# Allowed frontend origins (React, Next.js, Mobile apps)
origins = [
    "http://localhost:3000",       # React default port
    "http://localhost:5173",       # Vite default port
    "https://myproductionapp.com"  # Production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Allowed origin URLs
    allow_credentials=True,            # Allow cookies / Authorization headers
    allow_methods=["*"],               # Allow all HTTP verbs (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],               # Allow all request headers
)


# ==============================================================================
# 2. GLOBAL EXCEPTION HANDLER
# ==============================================================================
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    """
    Standardizes all HTTP error responses into a clean, unified enterprise format.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error_code": exc.status_code,
            "message": exc.detail,
            "path": str(request.url.path),
            "timestamp": datetime.utcnow().isoformat()
        }
    )


# ==============================================================================
# 3. SENSITIVE DATA FILTERING (response_model)
# ==============================================================================
# User internal database representation (Contains secret hashed_password):
MOCK_USER_DB = {
    101: {
        "id": 101,
        "username": "sachin_backend",
        "email": "sachin@dev.com",
        "hashed_password": "$2b$12$e8uq4f.9uH0J4fHkQ9Yv8OP18H73d9sYk111a4zY",  # SENSITIVE!
        "is_active": True,
        "role": "admin"
    }
}

# Public Safe Response Schema:
# NOTICE: 'hashed_password' is INTENTIONALLY EXCLUDED here!
class UserPublicResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    role: str

    model_config = ConfigDict(from_attributes=True)


@app.get(
    "/api/v1/users/{user_id}",
    response_model=UserPublicResponse,
    status_code=status.HTTP_200_OK,
    tags=["Production Users"]
)
def get_user_profile(user_id: int):
    """
    Returns user details while strictly withholding hashed_password from the response.
    """
    if user_id not in MOCK_USER_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} was not found."
        )

    # Even though we return the entire dictionary containing 'hashed_password',
    # FastAPI's response_model=UserPublicResponse filters it out automatically!
    return MOCK_USER_DB[user_id]

