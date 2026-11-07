"""
================================================================================
FASTAPI TUTORIAL #4: PATH PARAMETERS VS QUERY PARAMETERS & VALIDATION
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Path Parameters kya hote hain?
   - URL path ka hissa hote hain jo kisi specific resource ko identify karne ke liye 
     use hote hain.
   - Syntax: `@app.get("/users/{user_id}")`
   - Function parameter me same naam declare karna hota hai: `def get_user(user_id: int):`
   - **Automatic Type Conversion & Validation**:
     Agar client URL me `user_id=123` bhejega, toh Python me wo automatic integer `123` 
     ban jayega. Agar koi `user_id=abc` bhej dega, toh FastAPI automatically `422 Unprocessable Entity` 
     error return karega, specifying: *"Input should be a valid integer"*.

2. Path Order Matters (Order of Precedence Trap):
   - Agar aapke paas do endpoints hain:
     1. `/users/me` (Current logged-in user)
     2. `/users/{user_id}` (Any user by ID)
   - RULE: Fixed/Static path (`/users/me`) ko HAMESHA dynamic path (`/users/{user_id}`) se 
     PEHLE define karna padta hai!
   - Kyu? Agar `/users/{user_id}` pehle hoga, toh FastAPI `"me"` ko ek `user_id` maan 
     kar integer parse karne ki koshish karega aur fail ho jayega!

3. Query Parameters kya hote hain?
   - URL me question mark `?` ke baad aane wale key-value pairs ko Query Parameters kehte hain.
   - e.g. `http://127.0.0.1:8000/items?category=books&limit=10&page=1`
   - URL path me curly braces `{}` me declare NAHI hote, sirf function parameters me declare hote hain:
     `def get_items(category: str, limit: int = 10, skip: int = 0):`
   - Use Cases: Filtering, Sorting, Searching, Pagination.

4. Optional vs Required Query Parameters:
   - Required: `def get_item(q: str):` (Bina default value ke)
   - Optional: `def get_item(q: Optional[str] = None):` (Default `None` de diya)
   - With Default: `def get_item(limit: int = 20):` (Agar client na de toh 20 use hoga)

5. Parameter Validation with Path() & Query():
   - `Query(..., min_length=3, max_length=50)`: String length validation
   - `Path(..., ge=1, le=1000)`: Number range validation (ge = greater than or equal, le = less than or equal)
"""

from fastapi import FastAPI, Path, Query
from typing import Optional, List

app = FastAPI(
    title="Lecture 04 - Path & Query Parameters",
    description="Deep dive into Path Parameters, Query Parameters and Validation Constraints",
    version="1.0.0"
)

# In-memory mock database
MOCK_USERS_DB = {
    1: {"id": 1, "name": "Aman Sharma", "role": "admin", "city": "Delhi"},
    2: {"id": 2, "name": "Priya Singh", "role": "developer", "city": "Bangalore"},
    3: {"id": 3, "name": "Rohan Verma", "role": "developer", "city": "Pune"},
    4: {"id": 4, "name": "Sneha Patel", "role": "tester", "city": "Delhi"}
}


# ==============================================================================
# 1. PATH ORDER PRECEDENCE RULE
# ==============================================================================
# Static path pehle aana chahiye:
@app.get("/users/me", tags=["Users"])
def get_current_user_profile():
    """
    Current authenticated user profile (Static path)
    """
    return {
        "user_id": 999,
        "username": "sachin_logged_in",
        "email": "sachin@example.com",
        "status": "active"
    }


# Dynamic path parameters with Path() constraints:
@app.get("/users/{user_id}", tags=["Users"])
def get_user_by_id(
    user_id: int = Path(
        ...,
        title="The ID of the user to fetch",
        description="ID must be an integer >= 1 and <= 10000",
        ge=1,
        le=10000
    )
):
    """
    User details fetch karna by ID.
    Agar ID database me nahi mili toh not found response dega.
    """
    if user_id in MOCK_USERS_DB:
        return {"found": True, "data": MOCK_USERS_DB[user_id]}
    return {"found": False, "message": f"User with ID {user_id} not found."}


# ==============================================================================
# 2. QUERY PARAMETERS (Filtering & Pagination)
# ==============================================================================
@app.get("/users", tags=["Users"])
def filter_and_paginate_users(
    role: Optional[str] = Query(
        None,
        description="Filter users by role (admin, developer, tester)"
    ),
    city: Optional[str] = Query(
        None,
        description="Filter users by city"
    ),
    search: Optional[str] = Query(
        None,
        min_length=2,
        max_length=20,
        description="Search term in user's name"
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Maximum records to return (Pagination limit)"
    ),
    skip: int = Query(
        0,
        ge=0,
        description="Number of records to skip (Pagination offset)"
    )
):
    """
    Sabhi query parameters ko combine karke dynamic filtering aur pagination provide karta hai.
    Example URL: `/users?role=developer&city=Bangalore&limit=5`
    """
    results = list(MOCK_USERS_DB.values())

    # 1. Filter by role
    if role:
        results = [u for u in results if u["role"].lower() == role.lower()]

    # 2. Filter by city
    if city:
        results = [u for u in results if u["city"].lower() == city.lower()]

    # 3. Search by name keyword
    if search:
        results = [u for u in results if search.lower() in u["name"].lower()]

    # 4. Apply pagination (skip and limit)
    paginated_results = results[skip : skip + limit]

    return {
        "total_matches": len(results),
        "returned_count": len(paginated_results),
        "skip": skip,
        "limit": limit,
        "data": paginated_results
    }

