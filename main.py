import os
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# Validate API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Missing GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-pro")

# In-memory state store
fake_db = {}

class DecisionRequest(BaseModel):
    session_id: str | None = None
    user_input: str

@app.post("/decision")
def process_decision(data: DecisionRequest):
    session_id = data.session_id or str(uuid.uuid4())

    # Load or initialize state
    if session_id in fake_db:
        state = fake_db[session_id]
    else:
        state = {
            "risk_level": 50,
            "financial_impact": 0,
            "public_trust": 70
        }

    prompt = f"""
    You are a crisis simulation engine.
    Current state: {state}
    User decision: {data.user_input}
    Update the crisis state realistically and explain impact.
    """

    try:
        response = model.generate_content(prompt)
        ai_output = response.text
    except Exception as e:
        return {"error": str(e)}

    # Simple deterministic update logic
    state["risk_level"] += 10
    state["financial_impact"] += 50000
    state["public_trust"] -= 5

    fake_db[session_id] = state

    return {
        "session_id": session_id,
        "updated_state": state,
        "ai_response": ai_output
    }
