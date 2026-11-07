"""
================================================================================
FASTAPI TUTORIAL #20: PROTECTED ROUTES & ROLE-BASED ACCESS CONTROL (RBAC)
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Protected Routes kya hote hain?
   - Wo endpoints jinhe bina login kiye (bina valid JWT token ke) koi access nahi kar sakta.
   - Example: `/users/profile`, `/orders/place`, `/admin/dashboard`.
   - FastAPI me endpoint ko protect karne ke liye hum Dependency Injection use karte hain:
     `def get_profile(current_user: User = Depends(get_current_user)):`
   - Agar token missing ya invalid hua, toh function execute hi nahi hoga; dependency pehle hi 
     401 Unauthorized throw kar degi!

2. get_current_user Dependency Pattern:
   - Ye dependency:
     1. Request header se token extract karti hai.
     2. Token decode karke user email/id nikaalti hai.
     3. Database se actual User object fetch karti hai.
     4. Current User object hamare endpoint function ko inject kar deti hai!

3. Role-Based Access Control (RBAC):
   - Har user ke paas ek role hota hai (e.g. "admin", "customer", "moderator").
   - Protected endpoint ke andar hum check karte hain:
     `if current_user.role != "admin": raise HTTPException(403, "Forbidden: Admin access required!")`
   - Isse general users admin routes me ghusne se rok diye jaate hain.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta
from typing import Optional

SECRET_KEY = "my_ultra_secure_jwt_secret_key_change_in_production_2026"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Simulated User Database
USERS_DB = {
    "admin@company.com": {"id": 1, "name": "Sachin Admin", "email": "admin@company.com", "role": "admin", "active": True},
    "rahul@user.com": {"id": 2, "name": "Rahul Customer", "email": "rahul@user.com", "role": "user", "active": True},
    "blocked@user.com": {"id": 3, "name": "Banned User", "email": "blocked@user.com", "role": "user", "active": False}
}

app = FastAPI(
    title="Lecture 20 - Protected Routes & RBAC",
    description="Securing endpoints using Depends(get_current_user) and role-based authorization",
    version="1.0.0"
)

# Helper to issue tokens
def create_token(email: str, role: str) -> str:
    payload = {"sub": email, "role": role, "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ==============================================================================
# SECURITY DEPENDENCY: get_current_user
# ==============================================================================
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Validates token and injects the authenticated user model into the endpoint
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token payload invalid.")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials.")

    user = USERS_DB.get(email)
    if not user:
        raise HTTPException(status_code=401, detail="User belonging to this token no longer exists.")

    if not user.get("active", True):
        raise HTTPException(status_code=403, detail="User account is deactivated / banned!")

    return user


# Role Requirement Guard Dependency: Factory Pattern
def require_role(required_role: str):
    """Factory dependency that verifies user has the necessary authorization role"""
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user["role"] != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access Denied: Requires '{required_role}' privileges!"
            )
        return current_user
    return role_checker


# ==============================================================================
# ENDPOINTS
# ==============================================================================

# Helper endpoints to get tokens
@app.get("/tokens/admin", tags=["Auth Helpers"])
def get_admin_token():
    return {"token": create_token("admin@company.com", "admin")}

@app.get("/tokens/user", tags=["Auth Helpers"])
def get_user_token():
    return {"token": create_token("rahul@user.com", "user")}


# 1. PUBLIC ROUTE (Anyone can access)
@app.get("/public", tags=["Public"])
def public_endpoint():
    return {"message": "This is public information accessible without any login."}


# 2. PROTECTED USER ROUTE (Requires valid login token)
@app.get("/api/v1/profile/me", tags=["Protected User"])
def get_my_profile(current_user: dict = Depends(get_current_user)):
    """
    Protected Route: Injects authenticated user data
    """
    return {
        "status": "Authenticated",
        "welcome": f"Hello, {current_user['name']}!",
        "profile_data": current_user
    }


# 3. PROTECTED ADMIN ROUTE (Requires admin role)
@app.get("/api/v1/admin/dashboard", tags=["Protected Admin"])
def get_admin_dashboard(current_user: dict = Depends(require_role("admin"))):
    """
    Protected Route with RBAC: Only accessible to users with role='admin'.
    """
    return {
        "status": "Authorized",
        "secret_system_metrics": {
            "total_server_memory": "32 GB",
            "active_db_connections": 14,
            "security_alerts": 0
        },
        "admin": current_user["name"]
    }

