# AI Crisis Simulator

Real-time multimodal AI crisis simulation platform powered by Gemini Live API and Google Cloud. Enables leaders to stress-test high-stakes decisions through live voice interaction and persistent state tracking.

## Architecture

Client (Web / Voice UI)  
→ Cloud Run (FastAPI backend)  
→ Gemini Live API  
→ Firestore (state persistence)

## Reproducible Testing

### 1. Create virtual environment
python -m venv venv

### 2. Activate environment (Windows)
venv\Scripts\activate

### 3. Install dependencies
pip install fastapi uvicorn

### 4. Run server
uvicorn main:app --reload

### 5. Test API
curl -X POST "http://127.0.0.1:8000/decision" ^
-H "Content-Type: application/json" ^
-d "{\"choice\":\"option_a\"}"

### Expected JSON response
{
  "session_id": "uuid-string",
  "updated_state": {
    "risk_level": 60,
    "financial_impact": 50000,
    "public_trust": 65
  },
  "ai_response": "AI explanation of the decision impact..."
}
