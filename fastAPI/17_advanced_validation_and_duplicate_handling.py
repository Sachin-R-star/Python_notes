"""
================================================================================
FASTAPI TUTORIAL #17: ADVANCED VALIDATION & PASSWORD COMPLEXITY RULES
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Real-World Password Security Requirements:
   - Production level applications me simple password length check kaafi nahi hota.
   - NIST Security Guidelines ke mutabiq:
     * Kam se kam 8 characters.
     * Kam se kam 1 Uppercase letter (A-Z).
     * Kam se kam 1 Lowercase letter (a-z).
     * Kam se kam 1 Number / Digit (0-9).
     * Kam se kam 1 Special character (@, #, $, %, etc.).
   - Pydantic `@field_validator("password")` decorator me regex ya Python checks laga kar 
     hum strict validation enforce karte hain.

2. Password Confirmation (Confirm Password):
   - User se do baar password manga jata hai (`password` aur `confirm_password`).
   - Dono fields ko compare karne ke liye Pydantic v2 ka `@model_validator(mode='after')` 
     use hota hai. Ye poore model ke validate hone ke baad dono fields ko compare karta hai 
     aur mismatch hone par instant `ValueError("Passwords do not match!")` phenk deta hai!
"""

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
import re

app = FastAPI(
    title="Lecture 17 - Advanced Registration Validation",
    description="Password complexity validation and Confirm Password matching using Pydantic v2",
    version="1.0.0"
)

class UserRegisterAdvanced(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=64, description="Must be strong with upper, lower, digit & special char")
    confirm_password: str = Field(..., min_length=8, max_length=64)

    # 1. Field Validator: Password Complexity
    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter (A-Z)!")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter (a-z)!")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one numerical digit (0-9)!")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special character (!@#$%^&*)!")
        return v

    # 2. Model Validator: Compare password and confirm_password
    @model_validator(mode="after")
    def check_passwords_match(self) -> "UserRegisterAdvanced":
        if self.password != self.confirm_password:
            raise ValueError("Password and Confirm Password do not match!")
        return self


@app.post("/api/v1/auth/register-advanced", status_code=status.HTTP_201_CREATED, tags=["Authentication"])
def register_with_advanced_checks(user: UserRegisterAdvanced):
    """
    Advanced sign-up endpoint enforcing password complexity and matching confirm_password.
    """
    return {
        "status": "success",
        "message": f"User {user.username} successfully passed all security and complexity verifications!",
        "email": user.email
    }
