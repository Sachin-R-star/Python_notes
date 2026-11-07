"""
================================================================================
FASTAPI TUTORIAL #7: PROFESSIONAL PROJECT STRUCTURE & APIRouter MODULARIZATION
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Real-World Industry Folder Structure:
   - Jab aap company me production application banate ho, toh saara code ek single `main.py` me 
     nahi likhte. Agar 100 endpoints honge toh file 5000 lines ki ho jayegi jise maintain karna 
     impossible ho jayega.
   - Professional Modular Folder Structure:
     ```text
     my_fastapi_project/
     │
     ├── app/
     │   ├── __init__.py
     │   ├── main.py              # Application entry point, mounts all routers & middleware
     │   │
     │   ├── core/                # Configuration, security constants, JWT secret keys
     │   │   ├── config.py        # Pydantic BaseSettings (Reads .env file)
     │   │   └── security.py      # Password hashing & JWT token functions
     │   │
     │   ├── db/                  # Database connectivity & sessions
     │   │   ├── database.py      # SQLAlchemy engine, SessionLocal, Base
     │   │   └── init_db.py       # Table creation scripts
     │   │
     │   ├── models/              # SQLAlchemy ORM Models (Database Tables)
     │   │   ├── user.py
     │   │   └── task.py
     │   │
     │   ├── schemas/             # Pydantic Models (Request & Response validation)
     │   │   ├── user_schema.py
     │   │   └── task_schema.py
     │   │
     │   ├── api/                 # Endpoint Routers (APIRouter)
     │   │   ├── v1/
     │   │   │   ├── auth_router.py
     │   │   │   ├── user_router.py
     │   │   │   └── task_router.py
     │   │
     │   └── services/            # Business Logic & External API Helpers
     │       └── email_service.py
     │
     ├── .env                     # Secret environment variables (DB URLs, API Keys)
     ├── .gitignore
     └── requirements.txt
```

2. APIRouter kya hota hai?
   - `APIRouter` ek "Mini-FastAPI app" ki tarah hota hai.
   - Ye alag-alag modules ke endpoints ko group karta hai (e.g. Users ke saare routes `user_router` me, 
     Products ke `product_router` me).
   - Main app me hum simply use kar sakte hain:
     `app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])`
   - Prefix se baar-baar `/api/v1/users` likhne ki zaroorat nahi padti, router ke saare paths ke aage 
     prefix automatically jud jata hai!
"""

from fastapi import FastAPI, APIRouter, status
from pydantic import BaseModel
from typing import List

# ==============================================================================
# 1. USER ROUTER MODULE (Simulating app/api/v1/user_router.py)
# ==============================================================================
user_router = APIRouter(
    prefix="/users",            # Har route ke aage '/users' lag jayega
    tags=["Users Management"]   # Swagger UI grouping
)

class UserSchema(BaseModel):
    username: str
    email: str

@user_router.get("/", response_model=List[UserSchema])
def get_users_list():
    """Fetch list of all registered users"""
    return [
        {"username": "sachin_dev", "email": "sachin@example.com"},
        {"username": "jenny_cs", "email": "jenny@example.com"}
    ]

@user_router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_user(user: UserSchema):
    """Register a new user through the user router"""
    return {"message": f"User {user.username} successfully registered via APIRouter!"}


# ==============================================================================
# 2. ORDERS ROUTER MODULE (Simulating app/api/v1/order_router.py)
# ==============================================================================
order_router = APIRouter(
    prefix="/orders",
    tags=["Orders Processing"]
)

class OrderSchema(BaseModel):
    order_id: int
    item_name: str
    total_amount: float

@order_router.get("/")
def get_orders():
    """Fetch customer orders"""
    return [
        {"order_id": 1001, "item_name": "Python Backend Mastery Book", "total_amount": 499.0}
    ]



# ==============================================================================
# 3. MAIN APPLICATION (Simulating app/main.py)
# ==============================================================================
app = FastAPI(
    title="Lecture 07 - Production Project Structure & APIRouter",
    description="Demonstrating modular architecture using APIRouter and sub-applications",
    version="1.0.0"
)

# Mounting the modular routers onto the main app
# You can prefix them with API versions like /api/v1
app.include_router(user_router, prefix="/api/v1")
app.include_router(order_router, prefix="/api/v1")

@app.get("/")
def home():
    return {
        "status": "healthy",
        "registered_sub_routers": [
            "/api/v1/users",
            "/api/v1/orders"
        ],
        "tip": "Swagger UI (/docs) par jao aur dekho dono routers kaise alag-alag groups me categorize hue hain!"
    }

