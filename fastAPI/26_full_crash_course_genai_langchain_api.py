"""
================================================================================
FASTAPI TUTORIAL #26: FULL CRASH COURSE - BUILD & DEPLOY GENAI REST API (2026)
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. Full Crash Course Master Project Overview:
   - Ye hamara capstone master endpoint hai jo pure 26 videos ke concepts ko ek saath combine karta hai:
     1. FastAPI instance with OpenAPI documentation (`/docs`).
     2. Pydantic v2 validation (Data modeling, Prompt schemas, Field constraints).
     3. SQLAlchemy ORM database logging (Har prompt aur response ko database me save karna).
     4. GenAI Agent Engine (Prompt Templates, Simulated LLM Reasoning, Tool Execution).
     5. Token / Credit Usage Tracking.
     6. HTTP Status codes & error guards.

2. Production AI API Architecture:
   - Client sends prompt -> FastAPI validates via Pydantic -> Checks user quota -> 
     Invokes GenAI Model/Agent -> Formats response -> Saves chat history to Database -> 
     Returns clean JSON response!
"""

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Dict
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# ==============================================================================
# 1. DATABASE CONFIGURATION (CHAT & LLM HISTORY)
# ==============================================================================
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ChatInteraction(Base):
    __tablename__ = "chat_interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), index=True)
    prompt = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    model_name = Column(String(50), default="gemini-flash-2026")
    tokens_consumed = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================================================================
# 2. PYDANTIC SCHEMAS
# ==============================================================================
class AgentQueryRequest(BaseModel):
    user_id: str = Field(..., examples=["usr_98765"])
    prompt: str = Field(..., min_length=3, max_length=1000, examples=["Calculate total revenue for Q1 with 18% tax"])
    system_role: Optional[str] = Field("You are a helpful Financial AI Assistant", description="System prompt instructions")
    temperature: float = Field(0.7, ge=0.0, le=1.0)

class AgentQueryResponse(BaseModel):
    interaction_id: int
    user_id: str
    prompt: str
    ai_response: str
    tool_executed: Optional[str]
    tokens_consumed: int
    created_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


# ==============================================================================
# 3. GENAI AGENT & TOOL EXECUTION ENGINE
# ==============================================================================
def execute_agent_pipeline(prompt: str, system_role: str) -> tuple[str, Optional[str], int]:
    """
    Simulates AI Agent Tool Calling (e.g. LangChain Agent / ReAct Agent).
    Decides whether to perform mathematical computation tool or general answer.
    """
    tool_used = None
    tokens = len(prompt.split()) + 35

    # Simulated Tool Calling Detection
    if any(keyword in prompt.lower() for keyword in ["calculate", "tax", "revenue", "math"]):
        tool_used = "Financial_Math_Calculator_Tool"
        answer = (
            f"[{system_role}] Based on financial calculations, the Q1 computation executed via "
            f"'{tool_used}'. Results show strong quarter growth with optimized tax deductions."
        )
    else:
        answer = f"[{system_role}] I have processed your request: '{prompt}'. Everything is running smoothly on FastAPI."

    return answer, tool_used, tokens


# ==============================================================================
# 4. FASTAPI MASTER APP & ENDPOINTS
# ==============================================================================
app = FastAPI(
    title="Lecture 26 - GenAI & LangChain REST API Masterclass",
    description="End-to-End GenAI Agent REST API with Database Logging & Tool Execution",
    version="1.0.0"
)

@app.post(
    "/api/v1/genai/agent",
    response_model=AgentQueryResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["GenAI Master API"]
)
def run_ai_agent_endpoint(request: AgentQueryRequest, db: Session = Depends(get_db)):
    """
    End-to-End GenAI Agent Endpoint:
    1. Validates input schema.
    2. Runs reasoning engine & tool execution.
    3. Persists conversation history in database.
    4. Returns serialized response.
    """
    # 1. Execute AI Pipeline
    answer, tool, tokens = execute_agent_pipeline(request.prompt, request.system_role)

    # 2. Log Interaction to Database
    db_record = ChatInteraction(
        user_id=request.user_id,
        prompt=request.prompt,
        ai_response=answer,
        model_name="genai-agent-v1",
        tokens_consumed=tokens
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    # 3. Format response
    return {
        "interaction_id": db_record.id,
        "user_id": db_record.user_id,
        "prompt": db_record.prompt,
        "ai_response": db_record.ai_response,
        "tool_executed": tool,
        "tokens_consumed": db_record.tokens_consumed,
        "created_at": db_record.created_at
    }


@app.get(
    "/api/v1/genai/history/{user_id}",
    response_model=List[AgentQueryResponse],
    tags=["GenAI Master API"]
)
def get_user_chat_history(user_id: str, db: Session = Depends(get_db)):
    """
    Retrieves full historical interactions for a specific user.
    """
    records = db.query(ChatInteraction).filter(ChatInteraction.user_id == user_id).all()
    return [
        {
            "interaction_id": r.id,
            "user_id": r.user_id,
            "prompt": r.prompt,
            "ai_response": r.ai_response,
            "tool_executed": None,
            "tokens_consumed": r.tokens_consumed,
            "created_at": r.created_at
        }
        for r in records
    ]

