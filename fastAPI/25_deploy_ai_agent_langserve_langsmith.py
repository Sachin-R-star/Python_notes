"""
================================================================================
FASTAPI TUTORIAL #25: DEPLOY AI AGENT WITH FASTAPI, LANGSERVE & LANGSMITH
================================================================================

BRIEF HINGLISH EXPLANATION (Bada aur Aasan Explanation):
---------------------------------------------------------
1. GenAI / LLM Applications me FastAPI ka Role:
   - Aajkal sabhi top AI startups (OpenAI, Anthropic, HuggingFace) apne AI Models aur Agents 
     ko serve karne ke liye FastAPI use karte hain.
   - Kyu?
     1. Streaming Support: Token-by-token streaming (jaise ChatGPT type karta dikhta hai) 
        FastAPI me `StreamingResponse` (Server-Sent Events) ke through easily ban jati hai.
     2. Asynchronous concurrency: Multiple users jab ek saath LLM prompt bhejte hain, 
        toh async event loop block nahi hota.

2. LangServe kya hai?
   - LangChain community ka official deployment package jo kisi bhi LangChain Chain ya 
     AI Agent ko direct FastAPI route me expose kar deta hai:
     `add_routes(app, my_agent_chain, path="/agent")`
   - Automatically provide karta hai:
     * `/agent/invoke`: Single question-answer input.
     * `/agent/stream`: Live token-by-token streaming.
     * `/agent/batch`: Multiple prompts parallel me run karna.
     * Built-in Playground UI at `/agent/playground/`.

3. LangSmith Tracing & Observability:
   - Production AI agents me debugging ke liye:
     * LLM ne kya prompt receive kiya?
     * Kitne tokens kharch huye?
     * Response aane me kitni latency (seconds) lagi?
   - LangSmith automatically background me tracing telemetries log karta hai.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
import time
import asyncio
from typing import AsyncGenerator

app = FastAPI(
    title="Lecture 25 - AI Agent Deployment with FastAPI & LangServe",
    description="Serving GenAI LLM chains and token streaming endpoints with observability",
    version="1.0.0"
)

class PromptRequest(BaseModel):
    user_prompt: str = Field(..., min_length=2, examples=["Explain quantum computing in 2 lines."])
    temperature: float = Field(0.7, ge=0.0, le=2.0)

class AIResponse(BaseModel):
    prompt: str
    ai_response: str
    tokens_used: int
    execution_time_ms: float


# Simulated AI Reasoning Engine (Demonstrating LangChain Agent Workflow)
def run_ai_agent_reasoning(prompt: str) -> str:
    """Simulates multi-step chain-of-thought execution of an AI Agent"""
    return f"AI Agent Analysis: For the query '{prompt}', the optimal solution is to leverage asynchronous microservices."


# Streaming Token Generator (ChatGPT Style Live Streaming)
async def generate_llm_stream(prompt: str) -> AsyncGenerator[str, None]:
    """
    Simulates token-by-token streaming back to the client using Server-Sent Events.
    """
    response_tokens = [
        "Hello! ", "I ", "am ", "an ", "AI ", "Agent ", "running ", "on ", "FastAPI. ",
        "You ", "asked: ", f"'{prompt}'. ",
        "Streaming ", "responses ", "provide ", "zero-latency ", "user ", "experience!"
    ]

    for token in response_tokens:
        yield token
        await asyncio.sleep(0.1)  # Simulates token generation latency


# ==============================================================================
# ENDPOINTS
# ==============================================================================

# 1. STANDARD INVOCATION (Single Output)
@app.post("/api/v1/ai/invoke", response_model=AIResponse, tags=["GenAI Agent"])
def invoke_ai_agent(req: PromptRequest):
    """
    Standard synchronous invocation of AI Agent (LangServe invoke pattern)
    """
    start_time = time.time()
    agent_output = run_ai_agent_reasoning(req.user_prompt)
    latency_ms = (time.time() - start_time) * 1000

    return {
        "prompt": req.user_prompt,
        "ai_response": agent_output,
        "tokens_used": len(agent_output.split()),
        "execution_time_ms": round(latency_ms, 2)
    }


# 2. TOKEN STREAMING (ChatGPT-style SSE Stream)
@app.post("/api/v1/ai/stream", tags=["GenAI Agent"])
async def stream_ai_agent(req: PromptRequest):
    """
    Streams response token-by-token using StreamingResponse.
    Frontend can read this stream in real-time as words appear!
    """
    return StreamingResponse(
        generate_llm_stream(req.user_prompt),
        media_type="text/plain"
    )

