"""
================================================================================
FASTAPI TUTORIAL #6: PYDANTIC DATA VALIDATION & CRUD OPERATIONS
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Pydantic kya hai aur FastAPI me iski kya zaroorat hai?
   - Client jab JSON data bhejta hai (Request Body), toh backend developer ko 10 cheezein check karni padti hain:
     * Kya 'price' positive number hai?
     * Kya 'email' ka format sahi hai (@ aur .com hai)?
     * Kya mandatory fields missing toh nahi hain?
   - Traditional Flask/Django me ye sab manually `if-else` likh kar validate karna padta tha.
   - Pydantic ek data parsing aur validation library hai jo Python Type Hints use karke:
     1. Automatically JSON data ko Python Object me convert karti hai.
     2. Har field ka data type validate karti hai.
     3. Agar koi error ho, toh line number aur field name ke saath automatic detailed 422 JSON error return karti hai!

2. BaseModel:
   - Pydantic schema banane ke liye humari class `pydantic.BaseModel` se inherit karti hai:
     ```python
     class ProductSchema(BaseModel):
         name: str
         price: float
         in_stock: bool = True
```

3. Field() Validator:
   - `Field(...)` se hum advanced validation constraints laga sakte hain:
     * `gt=0`: Value must be greater than 0
     * `ge=18`: Value must be greater than or equal to 18
     * `min_length=3`, `max_length=50`: String length checks
     * `description="Product Price"`: Swagger docs me description show karta hai
     * `examples=[29.99]`: Swagger UI me pre-filled sample data dikhata hai!

4. Custom Validators (@field_validator):
   - Jab koi complex rule lagana ho (e.g., "Product name me special symbols nahi hone chahiye" 
     ya "Password me 1 uppercase hona zaroori hai"), tab hum `@field_validator` decorator use karte hain.

5. Nested Pydantic Models:
   - Ek model ke andar doosra model (e.g. `User` ke andar `Address` model, ya `Order` ke andar list of `Items`).
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List, Dict

app = FastAPI(
    title="Lecture 06 - Pydantic Validation & Full CRUD",
    description="Advanced Pydantic Schemas, Custom Field Validators and Error Handling",
    version="1.0.0"
)


# --- 1. Sub-Model (Nested Schema) ---
class Dimensions(BaseModel):
    length: float = Field(..., gt=0, description="Length in cm")
    width: float = Field(..., gt=0, description="Width in cm")
    height: float = Field(..., gt=0, description="Height in cm")


# --- 2. Main Product Schema with Advanced Validations ---
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, examples=["Wireless Gaming Headset"])
    description: Optional[str] = Field(None, max_length=500, examples=["RGB Noise-cancelling headset"])
    price: float = Field(..., gt=0, description="Price must be strictly positive", examples=[99.99])
    category: str = Field(..., examples=["Electronics"])
    in_stock: bool = Field(True, description="Stock availability status")
    contact_email: EmailStr = Field(..., description="Vendor contact email", examples=["vendor@shop.com"])
    dimensions: Optional[Dimensions] = None

    # Custom Field Validator for Business Logic
    @field_validator("name")
    @classmethod
    def validate_name_not_blank(cls, value: str):
        if value.strip() == "":
            raise ValueError("Product name cannot be empty or just spaces!")
        return value.title()  # Automatically convert to Title Case!


# Schema for Updating Product (All fields optional for PATCH)
class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    in_stock: Optional[bool] = None


# Response Schema (How data is returned to client)
class ProductResponse(ProductCreate):
    id: int


# Mock database
PRODUCTS_DB: Dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Mechanical Keyboard",
        "description": "Clicky Blue switches",
        "price": 59.99,
        "category": "Electronics",
        "in_stock": True,
        "contact_email": "support@keyboards.com",
        "dimensions": {"length": 44.0, "width": 13.5, "height": 3.8}
    }
}


# ==============================================================================
# CRUD ENDPOINTS
# ==============================================================================

# 1. READ ALL (GET)
@app.get("/products", response_model=List[ProductResponse], tags=["Products"])
def list_products():
    """Fetch all products currently in the database"""
    return list(PRODUCTS_DB.values())


# 2. CREATE (POST with Pydantic Validation)
@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product: ProductCreate):
    """
    Creates a new product with validated payload.
    Pydantic guarantees all fields match types and constraints before entering this function.
    """
    new_id = max(PRODUCTS_DB.keys(), default=0) + 1
    # .model_dump() converts Pydantic model to Python dictionary
    product_dict = product.model_dump()
    product_dict["id"] = new_id

    PRODUCTS_DB[new_id] = product_dict
    return product_dict


# 3. READ ONE (GET by ID)
@app.get("/products/{product_id}", response_model=ProductResponse, tags=["Products"])
def get_product(product_id: int):
    """Fetch single product by ID or return 404 HTTPException"""
    if product_id not in PRODUCTS_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} does not exist!"
        )
    return PRODUCTS_DB[product_id]


# 4. PARTIAL UPDATE (PATCH)
@app.patch("/products/{product_id}", response_model=ProductResponse, tags=["Products"])
def update_product(product_id: int, product_update: ProductUpdate):
    """Update only the specific fields provided in the request body"""
    if product_id not in PRODUCTS_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} does not exist!"
        )

    stored_product = PRODUCTS_DB[product_id]
    # exclude_unset=True ignores fields that were not provided in the incoming request
    update_data = product_update.model_dump(exclude_unset=True)

    stored_product.update(update_data)
    PRODUCTS_DB[product_id] = stored_product
    return stored_product


# 5. DELETE
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Products"])
def delete_product(product_id: int):
    """Delete a product from the database"""
    if product_id not in PRODUCTS_DB:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} does not exist!"
        )
    del PRODUCTS_DB[product_id]
    return None
