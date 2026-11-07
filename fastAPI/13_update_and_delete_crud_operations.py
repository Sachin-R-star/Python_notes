"""
================================================================================
FASTAPI TUTORIAL #13: UPDATE & DELETE DATABASE RECORDS (FULL CRUD COMPLETE)
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Database Record Update Karne Ka Sahi Tareeqa:
   - **Step 1: Check Karo Record Exist Karta Hai Ya Nahi**:
     Pehle ID se record fetch karo: `task = db.query(Task).filter(Task.id == task_id).first()`
     Agar nahi mila toh `HTTPException(404)` raise kar do.
   - **Step 2: Fields Update Karo**:
     Incoming Pydantic update model (`TaskUpdate`) se sirf wahi fields nikalo jo user ne 
     bheji hain:
     `update_data = task_update.model_dump(exclude_unset=True)`
     Aur har field ko existing ORM object par assign kar do:
     `for key, value in update_data.items(): setattr(task, key, value)`
   - **Step 3: Commit & Refresh**:
     * `db.commit()`: Changes ko database me update karta hai (`UPDATE tasks SET ... WHERE id=...`).
     * `db.refresh(task)`: Updated row ko reload karta hai.

2. Database Record Delete Karne Ka Tareeqa:
   - Step 1: Record dhundho. Nahi mila toh 404 raise karo.
   - Step 2: `db.delete(task)` call karo. (Ye session ko batata hai ki is row ko delete karna hai).
   - Step 3: `db.commit()` call karo taaki database se row permanently remove ho jaye (`DELETE FROM tasks WHERE id=...`).
   - Step 4: Status code `204 NO CONTENT` return karo (bina kisi body ke) ya `{"message": "Deleted successfully"}` with 200 OK.
"""

from fastapi import FastAPI, Depends, HTTPException, status, Path, Response
from pydantic import BaseModel, ConfigDict, Field
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
    __tablename__ = "tasks_demo_13"
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









# Pydantic Schemas
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


app = FastAPI(
    title="Lecture 13 - Complete CRUD: Update & Delete",
    description="PUT, PATCH and DELETE implementations with full SQLAlchemy database persistence",
    version="1.0.0"
)





# Startup seed
@app.on_event("startup")
def seed_initial_records():
    db = SessionLocal()
    if db.query(Task).count() == 0:
        db.add(Task(title="Initial Task 1", description="Learn SQL Update", completed=False))
        db.add(Task(title="Initial Task 2", description="Learn SQL Delete", completed=False))
        db.commit()
    db.close()


# ==============================================================================
# 1. UPDATE ENDPOINT (PATCH / PUT)
# ==============================================================================
@app.patch(
    "/tasks/{task_id}",
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK,
    tags=["CRUD Operations"]
)
def update_existing_task(
    task_id: int = Path(..., ge=1),
    task_update: TaskUpdate = ...,
    db: Session = Depends(get_db)
):
    """
    Updates specific fields of an existing task.
    """
    # 1. Find existing record
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot update: Task with ID {task_id} not found."
        )

    # 2. Extract only fields sent by user
    update_fields = task_update.model_dump(exclude_unset=True)

    # 3. Dynamically set updated attributes
    for field_name, new_value in update_fields.items():
        setattr(db_task, field_name, new_value)

    # 4. Save and reload
    db.commit()
    db.refresh(db_task)

    return db_task


# ==============================================================================
# 2. DELETE ENDPOINT
# ==============================================================================
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["CRUD Operations"]
)
def delete_existing_task(
    task_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
):
    """
    Deletes an existing task from the database.
    Returns HTTP 204 No Content on success.
    """
    # 1. Find existing record
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Cannot delete: Task with ID {task_id} not found."
        )

    # 2. Mark for deletion in session
    db.delete(db_task)

    # 3. Commit the deletion transaction
    db.commit()

    # 4. Return standard 204 empty response
    return Response(status_code=status.HTTP_204_NO_CONTENT)

