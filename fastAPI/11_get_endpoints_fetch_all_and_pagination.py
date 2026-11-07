"""
================================================================================
FASTAPI TUTORIAL #11: GET ENDPOINT WITH DATABASE - FETCH ALL & PAGINATION
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Database se Records Fetch Kaise Hote Hain?
   - SQLAlchemy ORM ka query syntax use karte hain:
     `tasks = db.query(Task).all()`
   - Ye SQL me internally execute karta hai:
     `SELECT tasks.id, tasks.title, tasks.completed, tasks.created_at FROM tasks;`
   - Aur har row ko ek `Task` Python object me convert karke list return karta hai.

2. Production me Pagination Kyu Mandatory Hai? (Interview Point):
   - Agar database me 100,000 tasks hain, aur aap direct `db.query(Task).all()` call karoge:
     1. Server ki saari RAM consume ho jayegi.
     2. Database par heavy load padega aur connection freeze ho sakta hai.
     3. Network par 50 MB ka JSON transfer hone me bohot time lagega.
   - Solution: **PAGINATION (skip & limit)**
     * `limit`: Ek page me maximum kitne records chahiye (e.g. 10 ya 20).
     * `skip` (offset): Kitne records chhod kar agla page shuru karna hai (e.g. Page 2 ke liye `skip=10`).
     * SQLAlchemy Syntax:
       `db.query(Task).offset(skip).limit(limit).all()`
     * SQL Equivalent:
       `SELECT * FROM tasks LIMIT 10 OFFSET 20;`

3. Filtering with Query Parameters:
   - Specific criteria par filter karna:
     `query = db.query(Task)`
     `if completed is not None: query = query.filter(Task.completed == completed)`
     `return query.offset(skip).limit(limit).all()`
"""

from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks_demo_11"
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

# Pydantic Response Schema
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


app = FastAPI(
    title="Lecture 11 - Fetch Data & Pagination",
    description="Fetching lists of records from DB with filtering and offset/limit pagination",
    version="1.0.0"
)

# Seed helper: Populate dummy records if DB is empty
@app.on_event("startup")
def populate_sample_data():
    db = SessionLocal()
    if db.query(Task).count() == 0:
        sample_tasks = [
            Task(title=f"Sample Task #{i}", description=f"Details for task {i}", completed=(i % 2 == 0))
            for i in range(1, 16)
        ]
        db.add_all(sample_tasks)
        db.commit()
    db.close()


@app.get(
    "/tasks",
    response_model=List[TaskResponse],
    tags=["Tasks DB"]
)
def fetch_all_tasks(
    db: Session = Depends(get_db),
    completed: Optional[bool] = Query(
        None,
        description="Filter tasks by completion status: True or False"
    ),
    search: Optional[str] = Query(
        None,
        description="Search keyword within task titles"
    ),
    skip: int = Query(
        0,
        ge=0,
        description="Number of records to skip (Offset)"
    ),
    limit: int = Query(
        10,
        ge=1,
        le=50,
        description="Number of records to return per page (Limit)"
    )
):
    """
    Fetch tasks with optional filtering and pagination.
    - Demonstrates db.query().filter().offset().limit().all()
    """
    # 1. Base query
    query = db.query(Task)

    # 2. Conditional filters
    if completed is not None:
        query = query.filter(Task.completed == completed)

    if search:
        # Case-insensitive substring search (ILIKE in Postgres, LIKE in SQLite)
        query = query.filter(Task.title.contains(search))

    # 3. Apply pagination (skip and limit) and execute query
    tasks = query.offset(skip).limit(limit).all()

    return tasks

