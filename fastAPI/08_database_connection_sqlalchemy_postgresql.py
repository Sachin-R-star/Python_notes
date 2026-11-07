"""
================================================================================
FASTAPI TUTORIAL #8: DATABASE CONNECTION (SQLAlchemy & PostgreSQL / SQLite)
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. SQLAlchemy kya hai?
   - SQLAlchemy Python ka sabse popular aur powerful ORM (Object Relational Mapper) hai.
   - Ye Python classes aur Database tables ke beech bridge ka kaam karta hai.
   - Iska faayda: Hume raw SQL queries (`SELECT * FROM users WHERE id=1`) likhne ki zaroorat 
     nahi padti, hum direct Python code (`db.query(User).filter(User.id == 1).first()`) likhte 
     hain aur SQLAlchemy internally database-specific SQL me convert kar deta hai!

2. 4 Golden Pillars of Database Setup in FastAPI:
   - A. **DATABASE_URL**:
     * PostgreSQL: `postgresql://username:password@localhost:5432/my_database`
     * SQLite (Local testing): `sqlite:///./fastapi_app.db`
   - B. **create_engine()**:
     * Database connection pool maintain karta hai. Real database se actual connection 
       establish karne ka main gateway hai.
   - C. **sessionmaker()**:
     * Database Session create karne wali factory. Ek "Session" ka matlab hota hai database ke 
       saath ek ongoing conversation (transaction).
   - D. **declarative_base() / Base**:
     * Ek base class jisse hamare saare database models (tables) inherit karte hain.

3. Dependency Injection with `yield` & `get_db()` (Production Standard):
   - Har HTTP request ke aane par ek naya Database Session khulna chahiye.
   - Request process hone ke baad wo Session **HAMESHA CLOSE** hona chahiye, chahe request 
     successful ho ya error throw kare!
   - Agar session close nahi karoge, toh connection leak ho jayega aur 100 users ke baad 
     database crash ho jayega (`Too many connections error`).
   - FastAPI isko `yield` generator function se solve karta hai:
     ```python
     def get_db():
         db = SessionLocal()  # 1. Connection khula
         try:
             yield db  # 2. Endpoint ko session provide kiya
         finally:
             db.close()  # 3. Request khatam hote hi GUARANTEED CLOSE!
```
"""

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ==============================================================================
# 1. DATABASE CONFIGURATION
# ==============================================================================
# For production PostgreSQL:
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password123@localhost:5432/fastapi_db"

# For portable, zero-setup execution, we use SQLite:
# (check_same_thread=False is needed only for SQLite because FastAPI handles multiple threads)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Engine creation
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# SessionLocal class
SessionLocal = sessionmaker(
    autocommit=False,  # Changes manually commit karne par hi save hongi (Safe!)
    autoflush=False,   # Unexpected flush se bachata hai
    bind=engine        # Engine se bind kiya
)


# Base class for all ORM Models
Base = declarative_base()


# ==============================================================================
# 2. DEPENDENCY INJECTION: get_db()
# ==============================================================================
def get_db():
    """
    Dependency generator function that yields a database session per request
    and guarantees safe closure in the 'finally' block.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Session close ho gaya, memory leak aur connection pool exhaustion avoided!


# ==============================================================================
# 3. FASTAPI TEST APP
# ==============================================================================
app = FastAPI(
    title="Lecture 08 - Database Connectivity & SQLAlchemy Setup",
    description="Engine, Sessionmaker, Base, and Dependency Injection get_db()",
    version="1.0.0"
)

@app.get("/db-health-check", tags=["Database"])
def test_db_connection(db: Session = Depends(get_db)):
    """
    Endpoint testing whether get_db dependency injects an active session
    """
    return {
        "status": "connected",
        "database_url": SQLALCHEMY_DATABASE_URL,
        "session_active": db.is_active,
        "message": "SQLAlchemy Database Session successfully initialized and ready for CRUD operations!"
    }

