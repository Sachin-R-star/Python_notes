"""
================================================================================
FASTAPI TUTORIAL #12: GET BY ID & EXCEPTION HANDLING WITH HTTPException
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Single Record Fetch Karna (`.first()` vs `.all()`):
   - Jab hum ID ke basis par fetch karte hain, toh hume list nahi balki SINGLE OBJECT chahiye hota hai:
     `task = db.query(Task).filter(Task.id == task_id).first()`
   - `.first()`:
     * SQL me internally `LIMIT 1` lagata hai.
     * Agar record mil gaya, toh ek single ORM Object return karega.
     * Agar record nahi mila, toh Python `None` return karega (Crash nahi hota!).

2. Error Handling in FastAPI: HTTPException:
   - Agar database me record nahi mila (`if not task:`), toh standard RESTful practice 
     kehta hai ki HTTP status **404 NOT FOUND** bhejni chahiye.
   - FastAPI me error raise karne ke liye hum `HTTPException` class use karte hain:
     ```python
     if not task:
         raise HTTPException(
             status_code=status.HTTP_404_NOT_FOUND,
             detail=f"Task with ID {task_id} was not found on the server."
         )
```
   - **`return` vs `raise`**:
     * Agar aap `return {"error": "not found"}` karoge, toh HTTP status code **200 OK** hi rahega!
       Frontend developer ka code bolega "Request Success", jo galat hai!
     * `raise HTTPException` karne se actual HTTP header me status 404 jata hai aur execution 
       turant ruk jata hai.
"""

from fastapi import FastAPI, Depends, HTTPException, status, Path
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks_demo_12"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


app = FastAPI(
    title="Lecture 12 - Get Record by ID & HTTPException",
    description="Fetching specific records by primary key with robust 404 error handling",
    version="1.0.0"
)

# Startup seed
@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    if db.query(Task).count() == 0:
        db.add(Task(title="Master Python Backend", description="Jenny & TechSimPlus combined", completed=True))
        db.add(Task(title="Build Portfolio API", description="Deploy on Railway or Render", completed=False))
        db.commit()
    db.close()


@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
    tags=["Tasks DB"]
)
def get_task_by_id(
    task_id: int = Path(..., ge=1, description="The positive integer ID of the task"),
    db: Session = Depends(get_db)
):
    """
    Fetch a single task record by its unique database ID.
    Raises HTTPException(404) if record does not exist.
    """
    # Query database using primary key filter and .first()
    task = db.query(Task).filter(Task.id == task_id).first()

    # Guard clause: Check if record exists
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found in database.",
            headers={"X-Error-Reason": "Invalid-ID"}  # Optional custom header
        )

    return task

