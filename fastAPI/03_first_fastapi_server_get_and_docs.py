"""
================================================================================
FASTAPI TUTORIAL #3: FIRST SERVER, GET ENDPOINT, SWAGGER UI & OPENAPI DOCS
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Anatomy of an API Endpoint in FastAPI:
   Endpoint likhne ke 3 mukhya hisse hote hain:
   ```python
   @app.get("/users")  # 1. Path Operation Decorator
   def get_users():  # 2. Path Operation Function
       return [...]  # 3. Response Content (JSON)
```

   - **Path / Endpoint**: URL ka wo hissa jo domain ke baad aata hai (e.g. `/users`, `/products`).
   - **Operation / HTTP Method**: Client kya action perform karna chahta hai (GET, POST, PUT, DELETE).
   - **Path Operation Function**: Wo Python function jo request aane par execute hota hai.

2. Automatic Interactive Documentation (FastAPI ki Sabse Badi Taqat):
   Bina kisi manual Swagger setup ya YAML file likhe, FastAPI automatically do documentation UI banata hai:
   - A. **Swagger UI (`http://127.0.0.1:8000/docs`)**:
     * Interactive documentation jahan aap browser se hi bina Postman ke kisi bhi API ko 
       test kar sakte ho ("Try it out" button dabakar).
     * Request body, parameters, aur responses live execute karke check kar sakte ho.
   - B. **ReDoc (`http://127.0.0.1:8000/redoc`)**:
     * Clean, publication-ready responsive documentation jo team members ya external clients 
       ko share karne ke liye best hoti hai.

3. OpenAPI Specification:
   - OpenAPI ek standardized schema format (JSON/YAML) hota hai jo batata hai ki aapki API 
     me kaun-kaun se endpoints hain, kya parameters expect karte hain aur kya return karte hain.
   - FastAPI automatically `http://127.0.0.1:8000/openapi.json` generate karta hai.

4. Function Docstrings & Tags:
   - Function ke neeche likhi gayi triple quotes `\"\"\"docstring\"\"\"` automatically Swagger UI 
     me description ban jati hai!
   - `tags=["Tag Name"]` parameter se Swagger UI me endpoints clean categories me group ho jate hain.
"""

from fastapi import FastAPI

app = FastAPI(
    title="My E-Commerce & User API",
    description="TechSimPlus Learnings Video #3: GET Endpoints and Swagger Documentation",
    version="1.0.0",
    docs_url="/docs",    # Swagger UI ka custom URL
    redoc_url="/redoc"   # ReDoc UI ka custom URL
)


# --- Endpoint 1: Root Greeting ---
@app.get("/", tags=["General"])
def root_endpoint():
    """
    ## Root Welcome Endpoint
    Ye endpoint server health aur welcome message return karta hai.
    - **Method**: GET
    - **Access**: Public
    """
    return {
        "message": "Welcome to FastAPI Backend API!",
        "version": "1.0.0",
        "documentation_links": {
            "swagger_ui": "/docs",
            "redoc": "/redoc",
            "openapi_schema": "/openapi.json"
        }
    }


# --- Endpoint 2: Static Products Listing ---
@app.get("/products", tags=["Products"])
def get_all_products():
    """
    ## Get All Products
    Sabhi available e-commerce products ki list return karta hai.
    """
    mock_products = [
        {"id": 1, "name": "Mechanical Keyboard", "price": 49.99, "in_stock": True},
        {"id": 2, "name": "Wireless Mouse", "price": 25.50, "in_stock": True},
        {"id": 3, "name": "4K Gaming Monitor", "price": 299.99, "in_stock": False}
    ]
    return {
        "total_products": len(mock_products),
        "data": mock_products
    }


# --- Endpoint 3: About Server & Developer Info ---
@app.get("/about", tags=["General"])
def get_about_info():
    """
    ## About Service
    API metadata aur backend developer credentials return karta hai.
    """
    return {
        "author": "Sachin R",
        "purpose": "Mastering FastAPI for High-Performance Backend Engineering",
        "year": 2026
    }
