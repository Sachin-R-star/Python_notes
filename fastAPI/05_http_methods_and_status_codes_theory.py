"""
================================================================================
FASTAPI TUTORIAL #5: HTTP METHODS & HTTP STATUS CODES COMPLETE GUIDE
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. HTTP Methods (HTTP Verbs) kya hote hain?
   - RESTful Architecture mein har HTTP method client ka "INTENT" (irada) batata hai:
   
   | HTTP Method | Operation | CRUD Equivalent | Idempotent? | Safe? |
   |-------------|-----------|-----------------|-------------|-------|
   | **GET**     | Read/Fetch data | READ | YES | YES |
   | **POST**    | Create new record | CREATE | NO | NO |
   | **PUT**     | Complete Replace/Update | UPDATE (Full) | YES | NO |
   | **PATCH**   | Partial Update | UPDATE (Partial) | NO | NO |
   | **DELETE**  | Remove record | DELETE | YES | NO |

2. Idempotency kya hoti hai? (Crucial Backend Interview Question):
   - **Idempotent Method**: Aisa method jise aap 1 baar call karo ya 100 baar call karo, 
     server ka final state SAME rehta hai (koi unexpected side effect nahi hota).
     * `GET`: 100 baar call karo, data sirf read hoga, kuch naya add nahi hoga (Idempotent).
     * `DELETE /items/5`: Pehli baar me item 5 delete ho jayega. Agli 99 baar me item 5 already 
       deleted hi rahega. State change nahi hogi (Idempotent).
     * `PUT /items/5`: Pura record replace karega. 10 baar same data replace karoge, state same rahegi.
     * `POST /items`: Har call par ek NAYA record banta jayega! 10 baar call karoge toh 10 naye 
       records create ho jayenge! (NOT IDEMPOTENT).

3. PUT vs PATCH ka Difference:
   - **PUT (Full Replacement)**: Agar user record me {name, age, city} hai, aur aap PUT bhejte ho 
     sirf `{name: "Rahul"}`, toh baaki fields null ya default ho sakti hain kyunki PUT pura replace karta hai.
   - **PATCH (Partial Update)**: Sirf specific fields ko update karta hai jo request me aayi hain, 
     baaki fields untouched rehti hain.

4. HTTP Status Codes Cheat Sheet (Standards & Best Practices):
   - **2xx Success**:
     * `200 OK`: Standard success response (GET, PUT, PATCH).
     * `201 Created`: Jab naya resource create ho jaye (POST).
     * `204 No Content`: Action successful hui par body me kuch return nahi karna (DELETE).
   - **4xx Client Errors**:
     * `400 Bad Request`: Client ne galat data ya malformed syntax bheja.
     * `401 Unauthorized`: Authentication missing ya invalid hai (Login required).
     * `403 Forbidden`: Authenticated toh ho, par permission nahi hai (e.g. Non-admin trying admin route).
     * `404 Not Found`: Requested resource exist nahi karta.
     * `422 Unprocessable Entity`: FastAPI ka signature validation error (Pydantic type mismatch).
   - **5xx Server Errors**:
     * `500 Internal Server Error`: Backend code crash ya unhandled exception.
     * `503 Service Unavailable`: Server overload ya maintenance me hai.
"""

from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI(
    title="Lecture 05 - HTTP Methods & Status Codes",
    description="Theoretical and Practical Demonstration of RESTful HTTP Verbs & Status Codes",
    version="1.0.0"
)

# Mock Store
IN_MEMORY_TASKS: Dict[int, dict] = {
    1: {"id": 1, "title": "Setup PostgreSQL", "completed": True},
    2: {"id": 2, "title": "Learn Pydantic Schemas", "completed": False}
}

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


# 1. GET: Fetching tasks with 200 OK
@app.get("/tasks", status_code=status.HTTP_200_OK, tags=["Tasks"])
def get_all_tasks():
    """GET Method: Safe and Idempotent"""
    return {"status": "success", "data": list(IN_MEMORY_TASKS.values())}


# 2. POST: Creating new task with 201 CREATED
@app.post("/tasks", status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task: TaskCreate):
    """POST Method: Not Idempotent (Creates new record each call)"""
    new_id = max(IN_MEMORY_TASKS.keys(), default=0) + 1
    new_task = {"id": new_id, "title": task.title, "completed": task.completed}
    IN_MEMORY_TASKS[new_id] = new_task
    return {"status": "created", "task": new_task}


# 3. PUT: Full update with 200 OK
@app.put("/tasks/{task_id}", status_code=status.HTTP_200_OK, tags=["Tasks"])
def replace_task(task_id: int, task: TaskCreate):
    """PUT Method: Replaces the entire resource state"""
    if task_id not in IN_MEMORY_TASKS:
        return {"error": "Task not found"}
    IN_MEMORY_TASKS[task_id] = {"id": task_id, "title": task.title, "completed": task.completed}
    return {"status": "replaced", "task": IN_MEMORY_TASKS[task_id]}


# 4. PATCH: Partial update with 200 OK
@app.patch("/tasks/{task_id}", status_code=status.HTTP_200_OK, tags=["Tasks"])
def partial_update_task(task_id: int, task: TaskUpdate):
    """PATCH Method: Updates only provided fields"""
    if task_id not in IN_MEMORY_TASKS:
        return {"error": "Task not found"}
    existing = IN_MEMORY_TASKS[task_id]
    if task.title is not None:
        existing["title"] = task.title
    if task.completed is not None:
        existing["completed"] = task.completed
    return {"status": "updated", "task": existing}


# 5. DELETE: Remove task with 204 NO CONTENT
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    """DELETE Method: Idempotent removal"""
    if task_id in IN_MEMORY_TASKS:
        del IN_MEMORY_TASKS[task_id]
    # 204 No Content response body should be empty
    return None

