"""
================================================================================
FASTAPI TUTORIAL #1: INTRODUCTION TO FASTAPI & MODERN BACKEND ARCHITECTURE
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. FastAPI kya hai?
   - FastAPI ek modern, ultra-fast (high performance) Python web framework hai jisse
     hum RESTful APIs aur backend services banate hain.
   - Isko create kiya tha Sebastián Ramírez ne (2018 mein).
   - Aaj ke time pe Netflix, Uber, Microsoft jaise tech giants apne production 
     microservices mein FastAPI use karte hain.

2. FastAPI itna popular kyu hai? (FastAPI vs Flask vs Django):
   - Traditional Frameworks (Flask, Django):
     * Django bohot heavy (monolithic) hai. Usme bohot si aisi cheezein pre-installed aati hain
       jo simple API banane ke liye zaroori nahi hoti.
     * Flask bohot lightweight hai, par usme asynchronous (async/await) support natively 
       achha nahi tha aur data validation ke liye alag se libraries lagani padti thi.
     * Dono mein API documentation (Swagger UI) manually banani padti thi.
   - FastAPI ka Magic:
     * Speed: NodeJS aur Go ke barabar performance (Starlette aur Uvicorn ki wajah se).
     * Automatic Documentation: Code likhte hi `/docs` (Interactive Swagger UI) aur 
       `/redoc` automatically generate ho jata hai bina 1 line extra likhe!
     * Automatic Data Validation: Python Type Hints aur Pydantic ki wajah se data types 
       galat aane par automatic helpful error messages deta hai.
     * Fewer Bugs: Type hints hone ki wajah se editor (VS Code) mein 100% autocompletion 
       aur bug detection pehle hi ho jati hai.

3. Core Foundations (FastAPI kin do kandhon par khada hai?):
   - A. Starlette:
     * Ek lightweight ASGI framework/toolkit hai jo web routing, websockets, aur background 
       tasks handle karta hai.
   - B. Pydantic:
     * Data validation aur serialization library jo Python type annotations use karti hai.
   - C. Uvicorn:
     * Lightning-fast ASGI web server jo hamare code ko execute karta hai.

4. WSGI vs ASGI (Interview Favorite Concept):
   - WSGI (Web Server Gateway Interface) - [Flask, Django]:
     * Synchronous hota hai. Ek request aayi toh thread block ho jata hai jab tak response 
       na mile (Blocking I/O). Agar database se data aane me 2 second lage toh server baaki 
       users ke liye wait karega.
   - ASGI (Asynchronous Server Gateway Interface) - [FastAPI]:
     * Asynchronous hota hai (`async/await`). Jab tak database ya third-party API se data 
       aa raha hai, tab tak server idle nahi baithta, balki baaki hazaron concurrent 
       requests ko serve karta rehta hai (Non-blocking I/O).

5. Real-World Analogy:
   - WSGI ek aisi dukan hai jahan ek time par sirf ek customer khada ho sakta hai. Jab tak 
     pehle customer ka samaan pack na ho, doosra customer wait karta rahega.
   - ASGI ek modern restaurant ki tarah hai jahan waiter order lekar chef ko de deta hai 
     aur turant agle customer ka order lene chala jata hai. Jaise hi khana taiyar hota hai, 
     wo table par serve kar deta hai!
"""

from fastapi import FastAPI
import sys

# Step 1: FastAPI Application ka instance create karna
# Ye app object hamari poori web application ka entry point hota hai
app = FastAPI(
    title="FastAPI Masterclass - Lecture 01",
    description="TechSimPlus Learnings Complete Playlist Backend Tutorials",
    version="1.0.0"
)


# Step 2: Ek basic root endpoint define karna
# @app.get("/") ek Path Operation Decorator hai
# Ye batata hai ki jab koi user root URL ('/') par HTTP GET request karega toh ye function chalega
@app.get("/")
def home():
    """
    Ye hamara pehla simple synchronous GET endpoint hai.
    FastAPI internally Python dictionaries ko standard JSON format me serialize karta hai.
    """
    return {
        "status": "success",
        "message": "Namaste dosto! Welcome to FastAPI Backend Course 2026",
        "framework": "FastAPI",
        "creator": "Sebastián Ramírez",
        "features": [
            "Automatic Swagger UI at /docs",
            "Automatic ReDoc at /redoc",
            "Data Validation via Pydantic",
            "High concurrency via ASGI & Uvicorn"
        ]
    }


# Step 3: Asynchronous endpoint ka example
# Jab hume database queries, external API calls, ya file reading karni hoti hai,
# tab hum 'async def' use karte hain taaki event loop block na ho.
@app.get("/async-info")
async def async_demonstration():
    """
    Async endpoint example: Non-blocking execution demo
    """
    return {
        "architecture": "ASGI (Asynchronous Server Gateway Interface)",
        "async_supported": True,
        "python_version": sys.version
    }


# Code Run Karne Ka Tareeqa:
# 1. Terminal open karo
# 2. Command chalao: uvicorn 01_fastapi_introduction_and_architecture:app --reload
# 3. Browser me open karo: http://127.0.0.1:8000
# 4. Interactive documentation dekho: http://127.0.0.1:8000/docs
