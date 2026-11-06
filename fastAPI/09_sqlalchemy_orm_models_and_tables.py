"""
================================================================================
FASTAPI TUTORIAL #9: SQLALCHEMY ORM MODELS & DATABASE TABLES CREATION
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. SQLAlchemy Models vs Pydantic Schemas (The Most Confusing Topic for Beginners!):
   Dono Python classes hoti hain, lekin dono ka role ALAG hota hai:
   
   | Feature | SQLAlchemy Model (`Base`) | Pydantic Schema (`BaseModel`) |
   |---------|---------------------------|-------------------------------|
   | **Kahan use hota hai?** | Database layer me (SQL Tables banane ke liye) | API Request / Response layer me (Validation ke liye) |
   | **Inheritance** | `class User(Base):` | `class UserCreate(BaseModel):` |
   | **Field Types** | `Column(Integer, primary_key=True)` | `id: int` |
   | **Kaam kya hai?** | Database me table create karna, queries execute karna | Incoming JSON ko validate karna, error throw karna |

2. Key Column Modifiers in SQLAlchemy:
   - `__tablename__ = "users"`: Database me table ka actual naam kya hoga.
   - `primary_key=True`: Is column ki value unique hogi aur har row ko uniquely identify karegi. 
     (SQLAlchemy integers ko automatically AUTO-INCREMENT karta hai).
   - `index=True`: Database is column par B-Tree index banayega taaki searching (`WHERE email='...'`) 
     100 guna tez ho jaye.
   - `unique=True`: Duplicate values allow nahi karega (e.g. Email ya Username duplicate na ho).
   - `nullable=False`: Ye field khali (NULL) nahi ho sakti (Mandatory field).
   - `default="default_value"`: Agar insert karte waqt value na di jaye toh default use hoga.
   - `server_default=func.now()`: Timestamp field jisme current server time automatically fill ho jata hai.

3. Tables Create Kaise Hoti Hain?
   - Command: `Base.metadata.create_all(bind=engine)`
   - Ye command SQLAlchemy ke registered sabhi models ko dekhti hai aur database me 
     corresponding `CREATE TABLE IF NOT EXISTS ...` SQL commands execute karti hai!
"""

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# ==============================================================================
# 1. USER ORM MODEL (TABLE: "users")
# ==============================================================================
class User(Base):
    __tablename__ = "users"

    # Primary Key Column (Auto-incrementing Integer ID)
    id = Column(Integer, primary_key=True, index=True)

    # Username: Indexed for fast login lookups, must be unique and non-null
    username = Column(String(50), unique=True, index=True, nullable=False)

    # Email: Must be unique across all accounts
    email = Column(String(100), unique=True, index=True, nullable=False)

    # Password Hash: Never store plain text passwords in database!
    hashed_password = Column(String(255), nullable=False)

    # Account Active Status flag (Default True)
    is_active = Column(Boolean, default=True)

    # User Role: 'user' or 'admin'
    role = Column(String(20), default="user")

    # Created At Timestamp: Automatically set by DB server on record creation
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# ==============================================================================
# 2. TASK / POST ORM MODEL (TABLE: "tasks")
# ==============================================================================
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False, index=True)
    description = Column(String(500), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# ==============================================================================
# 3. DATABASE INITIALIZATION SCRIPT
# ==============================================================================
if __name__ == "__main__":
    print("Connecting to local SQLite database...")
    engine = create_engine("sqlite:///./sql_app.db", echo=True)  # echo=True prints raw SQL queries!

    print("Creating all tables defined by SQLAlchemy Models...")
    # This inspects Base subclasses and executes CREATE TABLE
    Base.metadata.create_all(bind=engine)
    print("\nSUCCESS: Tables 'users' and 'tasks' created successfully in database!")
