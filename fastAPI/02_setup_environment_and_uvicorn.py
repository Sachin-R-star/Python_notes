"""
================================================================================
FASTAPI TUTORIAL #2: ENVIRONMENT SETUP, VIRTUALENV & UVICORN SERVER
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Virtual Environment kyu zaroori hai?
   - Har project ki apni dependencies aur package versions hote hain.
   - Maan lo Project A purane FastAPI version (0.68) par chal raha hai aur Project B 
     latest version (0.110+) par. Agar hum globally install karenge toh versions aapas 
     me lad padenge (dependency conflict).
   - Virtual Environment ek isolated boundary / sandbox bana deta hai jahan us project 
     ke saare packages alag folder me safe rehte hain bina system Python ko chhede.

2. Virtual Environment Setup Steps (Command Line):
   - Windows me:
     1. Virtual environment create karna:
        `python -m venv venv`
     2. Activate karna:
        `venv\\Scripts\\activate`
        (Jab terminal me `(venv)` aage likha dikhe, matlab environment active hai!)
     3. Deactivate karna:
        `deactivate`
   - Mac / Linux me:
     `python3 -m venv venv`
     `source venv/bin/activate`

3. Essential Packages Install Karna:
   - `pip install fastapi`
     (FastAPI framework install karta hai)
   - `pip install "uvicorn[standard]"`
     (Uvicorn lightning-fast ASGI server install karta hai with uvloop aur httptools)
   - `pip freeze > requirements.txt`
     (Project ke sabhi installed packages ka record save karta hai taaki koi aur developer 
     `pip install -r requirements.txt` karke 1 minute me setup kar sake).

4. Uvicorn Command ka Breakdown:
   Command: `uvicorn main:app --reload --port 8000 --host 127.0.0.1`
   - `main`: Python file ka naam (`main.py` bina .py extension ke).
   - `app`: `main.py` file ke andar banaya gaya FastAPI instance (`app = FastAPI()`).
   - `--reload`: Hot-Reloading flag! Jab bhi aap code change karke Ctrl+S karoge, 
     server automatically restart ho jayega bina manual restart kiye. 
     (NOTE: `--reload` sirf development ke liye hota hai, production me use nahi karte!)
   - `--port`: Port number (Default: 8000).
   - `--host`: Host IP (127.0.0.1 matlab localhost).

5. Programmatic Execution:
   - Server ko terminal se command likhne ke alawa direct Python script ke andar 
     `if __name__ == '__main__': uvicorn.run(...)` likhkar bhi start kiya ja sakta hai!
"""

from fastapi import FastAPI
import uvicorn

# FastAPI app instance
app = FastAPI(
    title="Lecture 02 - Setup & Uvicorn Server",
    description="Understanding Uvicorn server flags, ports and environment configuration",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    Sample server health check endpoint
    """
    return {
        "status": "online",
        "server": "Uvicorn ASGI Server",
        "environment": "Development",
        "hot_reload": True,
        "tip": "Ctrl+C dabane par server cleanly shut down ho jayega."
    }

@app.get("/environment-steps")
def get_setup_guide():
    return {
        "step_1": "python -m venv venv",
        "step_2": "venv\\Scripts\\activate (Windows) ya source venv/bin/activate (Mac/Linux)",
        "step_3": "pip install fastapi uvicorn",
        "step_4": "uvicorn <filename>:app --reload"
    }


# Programmatic server startup:
# Agar hum direct is file ko run karein: `python 02_setup_environment_and_uvicorn.py`,
# toh uvicorn.run() automatically server ko start kar dega!
if __name__ == "__main__":
    print("Starting Uvicorn Server programmatically on http://127.0.0.1:8000 ...")
    uvicorn.run(
        "02_setup_environment_and_uvicorn:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

