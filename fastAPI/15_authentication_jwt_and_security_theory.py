"""
================================================================================
FASTAPI TUTORIAL #15: AUTHENTICATION, AUTHORIZATION & JWT SECURITY THEORY
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Authentication vs Authorization (Top Interview Question):
   - **Authentication (AuthN) - "Aap Kaun Ho?"**:
     * User ki identity verify karna (Username + Password, OTP, FaceID).
     * Example: Airport security par apna passport aur ticket dikhana.
   - **Authorization (AuthZ) - "Aapko Kya Permission Hai?"**:
     * Verified user kya-kya action kar sakta hai wo check karna (Roles & Permissions).
     * Example: Airport me verified hone ke baad bhi aap Pilot cabin me nahi ja sakte, 
       sirf apni passenger seat par baith sakte ho.

2. Password Hashing (Bcrypt & Salt):
   - NEVER EVER store plain passwords in database!
   - Agar database hack ho gaya toh sabhi users ke passwords chori ho jayenge.
   - **Hashing vs Encryption**:
     * Encryption Two-way hota hai (Encrypt -> Decrypt).
     * Hashing ONE-WAY mathematical function hota hai (Data -> Hash). Hash se wapas original 
       password calculate karna mathematically impossible hota hai!
   - **Salt**: Random random characters jo hashing se pehle password me chipkaye jaate hain 
     taaki "Rainbow Table Attacks" fail ho jayein.
   - Standard Library: `passlib` with `bcrypt`.

3. JWT (JSON Web Token) Deep Dive:
   - Stateless Token-based authentication standard.
   - Server session memory me store nahi karta. Token client (browser/app) ke paas rehta hai.
   - Ek JWT me 3 hisse hote hain jo dot `.` se jude hote hain:
     `AAAAAA . BBBBBB . CCCCCC`
     * **1. Header (Red)**: Algorithm ka naam (e.g. HS256) aur token type ("JWT").
     * **2. Payload (Purple)**: Actual claims/data (e.g. `user_id`, `email`, `role`, `exp` expiration time).
       (NOTE: Payload encrypted nahi hota, sirf base64 encoded hota hai! Sensitive data jaise 
       credit card ya password kabhi payload me mat daalna!).
     * **3. Signature (Blue)**:
       `HMACSHA256(base64UrlEncode(Header) + "." + base64UrlEncode(Payload), SECRET_KEY)`
       Ye sabse critical hissa hai! Agar hacker payload me `role: "user"` ko badal kar `role: "admin"` 
       kar dega, toh Signature match nahi hoga aur server request turant REJECT kar dega!

4. Secret Key & Expiration:
   - `SECRET_KEY`: Server ka private secret jo sirf server ko pata hota hai.
   - `ALGORITHM`: Usually "HS256".
   - `exp` (Expiration): Token kitne time baad expire hoga (e.g. 30 minutes). Expire hone ke 
     baad user ko re-login karna padega.
"""

import hmac
import hashlib
import base64
import json
import time

def demo_jwt_creation_simulation():
    """
    Demonstrating how JWT Signature prevents tampering under the hood.
    """
    SECRET_KEY = "super_secret_enterprise_encryption_key_2026"

    # Part 1: Header
    header = {"alg": "HS256", "typ": "JWT"}
    header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")

    # Part 2: Payload (Claims)
    payload = {
        "sub": "user_id_101",
        "email": "sachin@dev.com",
        "role": "student",
        "exp": int(time.time()) + 1800  # Expires in 30 minutes
    }
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")

    # Part 3: Signature
    unsigned_token = f"{header_b64}.{payload_b64}"
    signature = hmac.new(
        SECRET_KEY.encode(),
        unsigned_token.encode(),
        hashlib.sha256
    ).digest()
    sig_b64 = base64.urlsafe_b64encode(signature).decode().rstrip("=")

    jwt_token = f"{unsigned_token}.{sig_b64}"

    print("==================================================")
    print("        UNDER THE HOOD: JWT ANATOMY               ")
    print("==================================================")
    print("1. Header (B64)    :", header_b64)
    print("2. Payload (B64)   :", payload_b64)
    print("3. Signature (B64) :", sig_b64)
    print("\nFull Assembled JWT Token:")
    print(jwt_token)

    # TAMPERING ATTACK SIMULATION:
    # Maan lo kisi hacker ne client side par token modify kiya aur 'role' ko 'admin' bana diya:
    tampered_payload = dict(payload)
    tampered_payload["role"] = "SUPER_ADMIN"
    tampered_payload_b64 = base64.urlsafe_b64encode(json.dumps(tampered_payload).encode()).decode().rstrip("=")

    tampered_token = f"{header_b64}.{tampered_payload_b64}.{sig_b64}"

    # Server verification:
    recomputed_sig = base64.urlsafe_b64encode(
        hmac.new(SECRET_KEY.encode(), f"{header_b64}.{tampered_payload_b64}".encode(), hashlib.sha256).digest()
    ).decode().rstrip("=")

    print("\n--- Tampering Verification Test ---")
    print("Is Tampered Token Valid?", recomputed_sig == sig_b64)
    print("Result: Server detected mismatch! Tampered request instantly rejected with 401 Unauthorized.")

if __name__ == "__main__":
    demo_jwt_creation_simulation()
