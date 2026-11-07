"""
================================================================================
FASTAPI TUTORIAL #19: TOKEN-BASED AUTHENTICATION & JWT DECODING
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Request Se Token Extract Kaise Hota Hai?
   - Client jab request bhejta hai, toh HTTP Headers me bhejta hai:
     `Authorization: Bearer <eyJhbGciOiJIUzI1NiIsInR5cCI...>`
   - FastAPI iske liye built-in class deta hai: `OAuth2PasswordBearer(tokenUrl="login")`.
   - Ye dependency automatically request headers me se "Bearer " prefix hata kar 
     pure JWT string extract kar leti hai. Agar header missing ho toh automatic 401 throw karti hai.

2. JWT Decode & Verification Process:
   - Command: `payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])`
   - Ye function 3 cheezein automatically verify karta hai:
     1. Kya signature valid hai? (Agar token me 1 character bhi badla gaya ho toh `InvalidSignatureError`).
     2. Kya token expire ho chuka hai? (Current time > `exp` time hone par `ExpiredSignatureError`).
     3. Kya header me specified algorithm match kar raha hai?
   - Agar sab valid hai, toh decoded dictionary (`payload`) return karta hai jisme se hum 
     `user_id` ya `email` nikal lete hain!
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my_ultra_secure_jwt_secret_key_change_in_production_2026"
ALGORITHM = "HS256"

# OAuth2 scheme pointing to login URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

app = FastAPI(
    title="Lecture 19 - JWT Decoding & Token Verification",
    description="Extracting Bearer tokens from request headers and validating JWT signatures",
    version="1.0.0"
)

# Helper function to generate test tokens easily
def generate_sample_token(email: str, minutes: int = 15) -> str:
    payload = {
        "sub": email,
        "role": "engineer",
        "exp": datetime.utcnow() + timedelta(minutes=minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# Token Decoding Function
def decode_and_verify_token(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Decodes the incoming Bearer JWT token and verifies signature & expiry.
    Raises HTTPException 401 if invalid or expired.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials or token signature invalid.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode and verify using the same SECRET_KEY and ALGORITHM
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session expired! Access token has expired. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise credentials_exception


# --- Endpoints ---
@app.get("/get-demo-token", tags=["Token Helpers"])
def get_demo_token():
    """Generates a valid test token for testing in Swagger UI"""
    token = generate_sample_token("sachin@dev.com", minutes=30)
    return {
        "sample_token": token,
        "instructions": "Copy this token, click 'Authorize' at the top of /docs and paste it!"
    }


@app.get("/api/v1/verify-my-token", tags=["Protected"])
def verify_token_endpoint(token_payload: dict = Depends(decode_and_verify_token)):
    """
    Protected endpoint: Only accessible if a valid Bearer token is passed in header.
    """
    return {
        "status": "Token Verified Successfully!",
        "authenticated_user_email": token_payload.get("sub"),
        "user_role": token_payload.get("role"),
        "full_token_claims": token_payload
    }

