"""
================================================================================
FASTAPI TUTORIAL #21: DATABASE RELATIONSHIPS - ONE-TO-MANY IN SQLALCHEMY
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Table Relationships kya hoti hain?
   - Real-world application me tables isolated nahi hoti, aapas me judi hoti hain:
     * One User -> Many Tasks / Posts / Orders (1:N One-to-Many)
     * One Student -> Many Courses & One Course -> Many Students (M:N Many-to-Many)
     * One User -> One Profile (1:1 One-to-One)

2. One-to-Many Relationship Setup in SQLAlchemy:
   - **Step 1: Child Table me ForeignKey Lagana**:
     * Task table ke andar `user_id` column banate hain:
       `user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)`
     * Ye batata hai ki task kis specific user ka hai.
   - **Step 2: SQLAlchemy relationship() Define Karna**:
     * Parent Model (`User`) ke andar:
       `tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")`
     * Child Model (`Task`) ke andar:
       `owner = relationship("User", back_populates="tasks")`
   - **Magic of back_populates**:
     * Ab aap Python me direct likh sakte ho:
       `user.tasks` -> Us user ke saare tasks ki list mil jayegi!
       `task.owner` -> Us task ke owner user ka pura object mil jayega!

3. Cascade Delete (`cascade="all, delete-orphan"`):
   - Agar hum kisi User ko delete karte hain, toh uske banaye huye saare tasks ka kya hoga?
   - Agar cascade set nahi hoga, toh database foreign key constraint error dega ya orphaned 
     tasks bache reh jayenge.
   - `cascade="all, delete-orphan"` set karne se jaise hi User delete hoga, uske saare tasks 
     bhi automatically database se safely delete ho jayenge!
"""

from fastapi import FastAPI, Depends, status
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Session

# Database setup
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ==============================================================================
# 1. ORM MODELS WITH 1-TO-MANY RELATIONSHIP
# ==============================================================================
class User(Base):
    __tablename__ = "rel_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True)

    # 1-to-Many: One user has many tasks
    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")


class Task(Base):
    __tablename__ = "rel_tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)

    # ForeignKey pointing to rel_users table 'id' column
    owner_id = Column(Integer, ForeignKey("rel_users.id", ondelete="CASCADE"), nullable=False)

    # Many-to-One: Each task has one owner
    owner = relationship("User", back_populates="tasks")


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================================================================
# 2. PYDANTIC SCHEMAS WITH NESTED RELATIONSHIPS
# ==============================================================================
class TaskSummary(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)

class UserWithTasksResponse(BaseModel):
    id: int
    name: str
    email: str
    tasks: List[TaskSummary] = []  # Automatically serializes relationship!

    model_config = ConfigDict(from_attributes=True)


app = FastAPI(
    title="Lecture 21 - SQLAlchemy Table Relationships (1:N)",
    description="One-to-Many relationship between Users and Tasks with cascading deletes",
    version="1.0.0"
)

# Seed helper to demonstrate relations
@app.on_event("startup")
def seed_related_data():
    db = SessionLocal()
    if db.query(User).count() == 0:
        u1 = User(name="Sachin", email="sachin@rel.com")
        db.add(u1)
        db.commit()
        db.refresh(u1)

        t1 = Task(title="Complete FastAPI Playlist", completed=True, owner_id=u1.id)
        t2 = Task(title="Learn LangChain GenAI API", completed=False, owner_id=u1.id)
        db.add_all([t1, t2])
        db.commit()
    db.close()


@app.get(
    "/users/{user_id}/with-tasks",
    response_model=UserWithTasksResponse,
    tags=["Relationships"]
)
def get_user_and_their_tasks(user_id: int, db: Session = Depends(get_db)):
    """
    Fetches user along with all associated tasks populated via relationship().
    """
    user = db.query(User).filter(User.id == user_id).first()
    return user
