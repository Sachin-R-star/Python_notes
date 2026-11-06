"""
================================================================================
FASTAPI TUTORIAL #23: HOW TO SEND EMAILS IN FASTAPI (SMTP & EMAIL TEMPLATES)
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. FastAPI me Email Sending Architecture:
   - Backend applications me emails bohot zaroori hote hain:
     * Welcome email after user registration.
     * Password reset link with secret token.
     * Order confirmation & invoice receipt.
   - Email bhejne ke liye hum **SMTP (Simple Mail Transfer Protocol)** use karte hain.
   - Provider Options:
     * Gmail SMTP (`smtp.gmail.com`, Port: 587 with TLS).
     * Production Services (SendGrid, AWS SES, Brevo, Mailgun).

2. Gmail App Passwords:
   - Google normal email password se direct login allow nahi karta.
   - Google Account Security me jaakar 2-Factor Authentication enable karke 
     ek 16-character ka **"App Password"** generate karna padta hai jo sirf hamare 
     FastAPI backend script ke liye valid hota hai.

3. Email Sending Implementation:
   - Python ka built-in `smtplib` aur `email.mime` module use kar sakte hain ya fir 
     `fastapi-mail` library.
   - Plain text ke saath-saath clean HTML templates (`MIMEMultipart("alternative")`) 
     bhejte hain taaki emails responsive aur professional lagein.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI(
    title="Lecture 23 - Email Service & SMTP Integration",
    description="Sending HTML and Plain-text emails via SMTP in FastAPI",
    version="1.0.0"
)

# SMTP Server Configurations (Normally stored in .env)
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"      # Replace with your email in production
SMTP_PASSWORD = "xxxx xxxx xxxx xxxx"  # 16-digit Google App Password


class EmailRequest(BaseModel):
    recipient_email: EmailStr
    subject: str
    recipient_name: str
    message_body: str


def send_smtp_email(to_email: str, subject: str, recipient_name: str, body: str, is_simulation: bool = True):
    """
    Sends email using standard smtplib and MIME protocols.
    In simulation mode, prints preview to avoid failing when dummy credentials are used.
    """
    if is_simulation:
        print("\n==================================================")
        print("          SIMULATED EMAIL DISPATCH                ")
        print("==================================================")
        print(f"TO      : {to_email}")
        print(f"SUBJECT : {subject}")
        print(f"BODY    : Hello {recipient_name},\n{body}")
        print("==================================================\n")
        return True

    # Real SMTP Network Call
    msg = MIMEMultipart("alternative")
    msg["From"] = SMTP_USER
    msg["To"] = to_email
    msg["Subject"] = subject

    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
          <h2 style="color: #2b6cb0;">Welcome to Python FastAPI Masterclass!</h2>
          <p>Hi <strong>{recipient_name}</strong>,</p>
          <p>{body}</p>
          <hr style="border: none; border-top: 1px solid #eee;">
          <p style="font-size: 12px; color: #888;">This is an automated notification from FastAPI Backend Service.</p>
        </div>
      </body>
    </html>
    """

    part1 = MIMEText(body, "plain")
    part2 = MIMEText(html_content, "html")
    msg.attach(part1)
    msg.attach(part2)

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()  # Secure the connection with TLS encryption
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, to_email, msg.as_string())
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"SMTP Email Delivery Failed: {str(e)}"
        )


@app.post("/api/v1/send-email", status_code=status.HTTP_200_OK, tags=["Notifications"])
def send_notification_email(req: EmailRequest):
    """
    Endpoint triggering an email dispatch to recipient.
    """
    success = send_smtp_email(
        to_email=req.recipient_email,
        subject=req.subject,
        recipient_name=req.recipient_name,
        body=req.message_body,
        is_simulation=True  # Simulated by default for instant safe execution
    )
    return {
        "status": "success",
        "message": f"Email successfully dispatched to {req.recipient_email}",
        "subject": req.subject
    }
