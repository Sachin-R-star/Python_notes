"""
================================================================================
FASTAPI TUTORIAL #22: USER ASSOCIATION - CREATE TASKS FOR LOGGED-IN USERS
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. User Association kya hota hai?
   - Jab koi user login karke naya task banata hai (`POST /tasks`), toh request body me 
     user se `user_id` nahi manga jata!
     (Kyunki koi bhi user kisi doosre ki ID bhej kar fake task bana sakta hai!).
   - Sahi Tareeqa:
     `user_id` hum **JWT Token** se nikaalte hain jo `Depends(get_current_user)` se automatically 
     backend me inject hota hai!
     `new_task = Task(title=data.title, owner_id=current_user.id)`

2. User Isolation & Data Security:
   - Jab user `GET /tasks` kare, toh use database ke saare tasks nahi dikhne chahiye; 
     sirf USKE APNE tasks dikhne chahiye:
     `tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()`

3. Preventing Cross-User Access (Ownership Verification):
   - Agar User A kisi task ko delete ya update karne ki koshish kare jo User B ka hai:
     ```python
     task = db.query(Task).filter(Task.id == task_id).first()
     if task.owner_id != current_user.id:
         raise HTTPException(
             status_code=403,
             detail="Not authorized to perform this action on someone else's task!",
         )
```
   - Ye check multi-tenant SaaS applications me bohot critical hota hai.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

# Simulated In-Memory Database for demonstration
MOCK_USERS = {
    1: {"id": 1, "username": "sachin_dev", "token": "token_sachin"},
    2: {"id": 2, "username": "rahul_user", "token": "token_rahul"}
}

MOCK_TASKS = {
    101: {"id": 101, "title": "Sachin's Private Project Plan", "owner_id": 1},
    102: {"id": 102, "title": "Sachin's Second Task", "owner_id": 1},
    103: {"id": 103, "title": "Rahul's College Assignment", "owner_id": 2}
}

app = FastAPI(
    title="Lecture 22 - User Association & Protected CRUD",
    description="Associating created records automatically with the authenticated user ID",
    version="1.0.0"
)

# Mock Current User Dependency (Simulating Token Auth)
def get_current_user(token: str):
    for u in MOCK_USERS.values():
        if u["token"] == token:
            return u
    raise HTTPException(status_code=401, detail="Invalid token!")

class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    owner_id: int


# ==============================================================================
# ENDPOINTS
# ==============================================================================

# 1. CREATE TASK ASSOCIATED WITH CURRENT USER
@app.post("/my-tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED, tags=["User Tasks"])
def create_task_for_me(task_in: TaskCreate, token: str = "token_sachin"):
    """
    Creates task where owner_id is automatically assigned from the authenticated user token.
    """
    user = get_current_user(token)

    new_id = max(MOCK_TASKS.keys(), default=0) + 1
    new_task = {
        "id": new_id,
        "title": task_in.title,
        "owner_id": user["id"]  # Securely mapped from token!
    }
    MOCK_TASKS[new_id] = new_task
    return new_task


# 2. FETCH ONLY CURRENT USER'S TASKS
@app.get("/my-tasks", response_model=List[TaskOut], tags=["User Tasks"])
def get_my_tasks(token: str = "token_sachin"):
    """
    Fetches ONLY the tasks owned by the current logged-in user.
    """
    user = get_current_user(token)

    # Filter tasks by owner_id
    user_tasks = [t for t in MOCK_TASKS.values() if t["owner_id"] == user["id"]]
    return user_tasks


# 3. DELETE WITH STRICT OWNERSHIP CHECK
@app.delete("/my-tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["User Tasks"])
def delete_my_task(task_id: int, token: str = "token_sachin"):
    """
    Deletes task only if it belongs to the authenticated user.
    Throws 403 Forbidden if user attempts to delete another user's task.
    """
    user = get_current_user(token)

    if task_id not in MOCK_TASKS:
        raise HTTPException(status_code=404, detail="Task not found")

    task = MOCK_TASKS[task_id]

    # Crucial Ownership Authorization Check
    if task["owner_id"] != user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: You cannot delete someone else's task!"
        )

    del MOCK_TASKS[task_id]
    return None
