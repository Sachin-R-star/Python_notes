"""
================================================================================
FASTAPI TUTORIAL #24: BACKGROUND TASKS - ASYNC BACKGROUND PROCESSING
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Background Tasks kya hote hain aur inki kyu zaroorat hai?
   - Maan lo user ne "Place Order" button dabaya.
   - Server ko 3 kaam karne hain:
     1. Database me order save karna (Takes 50ms).
     2. Payment gateway confirm karna (Takes 100ms).
     3. Customer ko Confirmation Email bhejna + PDF invoice generate karna (Takes 4000ms / 4 Seconds!).
   - Agar aap ye sab ek ke baad ek (synchronously) karoge, toh user ka browser 4.2 seconds tak 
     ghoomta rahega (Loading spinner!). User sochega website hang ho gayi hai.
   - **Background Tasks ka Magic**:
     * Database me order save karo.
     * Email/PDF generation ko **Background Task** me schedule kar do.
     * Aur user ko 150ms ke andar instant response bhej do: `{"status": "Order Placed Successfully!"}`.
     * User ka browser khush, aur server background me aaram se email deliver karta rahega!

2. FastAPI's Built-in BackgroundTasks vs Celery (Interview Comparison):
   - **FastAPI BackgroundTasks**:
     * Zero external setup (Redis ya RabbitMQ ki zaroorat nahi hai).
     * Same process ke event loop me run hota hai.
     * Best for: Sending emails, logging events, updating read counters, quick notifications.
   - **Celery + Redis / RabbitMQ**:
     * Distributed task queue jo heavy computing (Video transcoding, Machine Learning model training, 
       massive data exports) ke liye alag worker servers par execute hota hai.

3. BackgroundTasks Implementation:
   - Endpoint parameter me declare karo: `background_tasks: BackgroundTasks`.
   - Task schedule karo: `background_tasks.add_task(task_function, arg1, arg2)`.
   - FastAPI pehle response return karega, fir background task execute karega!
"""

from fastapi import FastAPI, BackgroundTasks, status
from pydantic import BaseModel, EmailStr
import time

app = FastAPI(
    title="Lecture 24 - Background Tasks in FastAPI",
    description="Running heavy operations like email sending and report generation asynchronously in the background",
    version="1.0.0"
)

# Long-running background worker function
def process_heavy_task_in_background(task_name: str, recipient: str, duration_seconds: int = 3):
    """
    Simulates a time-consuming background process (e.g. Email sending, PDF report rendering)
    """
    print(f"\n[BACKGROUND WORKER STARTED] Executing '{task_name}' for {recipient}...")
    time.sleep(duration_seconds)  # Simulating heavy network or CPU I/O
    print(f"[BACKGROUND WORKER COMPLETED] '{task_name}' successfully finished for {recipient}!\n")


class OrderRequest(BaseModel):
    customer_name: str
    email: EmailStr
    item: str
    amount: float


@app.post(
    "/api/v1/orders/checkout",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Checkout"]
)
def checkout_order(order: OrderRequest, background_tasks: BackgroundTasks):
    """
    Demonstrates instant HTTP 202 response while scheduling heavy email dispatch in the background.
    """
    # 1. Immediate business action: Order saved to database (simulated)
    order_id = 98452
    print(f"Order #{order_id} saved to database instantly.")

    # 2. Schedule the heavy email dispatch to run in background
    # Notice: We pass function reference WITHOUT parentheses (), followed by its arguments:
    background_tasks.add_task(
        process_heavy_task_in_background,
        task_name="Generate Invoice PDF & Dispatch Email",
        recipient=order.email,
        duration_seconds=3
    )

    # 3. Return immediate response to customer (Zero waiting time!)
    return {
        "status": "success",
        "order_id": order_id,
        "message": "Your order has been placed! An invoice is being generated and emailed in the background.",
        "customer": order.customer_name,
        "item": order.item
    }

