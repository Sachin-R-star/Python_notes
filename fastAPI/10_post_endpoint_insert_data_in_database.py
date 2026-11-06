"""
================================================================================
FASTAPI TUTORIAL #10: POST ENDPOINT WITH DATABASE - INSERT DATA
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Database me Data Insert Karne Ka 4-Step Process:
   - **Step 1: Pydantic Validation**:
     User jo JSON payload bhejta hai, pehle Pydantic schema (`TaskCreate`) use validate 
     karta hai ki fields aur types valid hain ya nahi.
   - **Step 2: SQLAlchemy Model Object Banana**:
     Pydantic data ko unpack karke SQLAlchemy ORM Model class ka ek naya instance banate hain:
     `new_task = Task(**task.model_dump())`
   - **Step 3: Database Session me Add & Commit karna**:
     * `db.add(new_task)`: Session me object ko staging area me daalta hai (jaise Git add).
     * `db.commit()`: Transaction ko permanently database disk me save karta hai (jaise Git commit).
   - **Step 4: Object Refresh karna**:
     * `db.refresh(new_task)`:
       Ye bohot important line hai! Database commit hone ke baad database ne jo auto-generated 
       fields generate kiye (jaise primary key `id`, auto timestamp `created_at`), un values ko 
       wapas hamare Python object me load kar leta hai!

2. Response Model (`response_model=TaskResponse`):
   - Hum database se nikla hua object seedhe client ko bhej sakte hain.
   - Pydantic v2 me `model_config = ConfigDict(from_attributes=True)` (ya Pydantic v1 me `orm_mode = True`) 
     likhne se Pydantic SQLAlchemy ORM objects ke attributes ko automatically JSON me convert kar deta hai!
"""

from fastapi import FastAPI, Depends, status
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# --- Database Setup ---
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- SQLAlchemy Model ---
class Task(Base):
    __tablename__ = "tasks_demo_10"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --- Pydantic Schemas ---
# 1. Incoming Request Payload Schema
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=100, examples=["Learn FastAPI Database Integration"])
    description: Optional[str] = Field(None, max_length=255, examples=["Complete videos 8 to 14"])
    completed: bool = Field(False, description="Initial task completion state")

# 2. Outgoing Response Schema
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: Optional[datetime]

    # Crucial configuration for SQLAlchemy ORM compatibility:
    model_config = ConfigDict(from_attributes=True)


# --- FastAPI Application ---
app = FastAPI(
    title="Lecture 10 - Database Insertion (POST Endpoint)",
    description="Saving Pydantic validated data into SQLite/PostgreSQL with SQLAlchemy",
    version="1.0.0"
)

@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks DB"]
)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    """
    Inserts a new task row into the database.
    - **task**: Validated via TaskCreate Pydantic schema
    - **db**: Injected SQLAlchemy Session via get_db dependency
    """
    # 1. Create SQLAlchemy ORM model instance from Pydantic model
    db_task = Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    # 2. Stage the object in the database session
    db.add(db_task)

    # 3. Commit changes to permanently save in DB
    db.commit()

    # 4. Refresh to retrieve auto-generated columns (like id and created_at)
    db.refresh(db_task)

    # 5. Return the ORM object (FastAPI serializes it using TaskResponse)
    return db_task
