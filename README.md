# AI Crisis Simulator

Local FastAPI decision endpoint for crisis-response policy exploration: POST a decision, get back updated crisis state plus a Gemini-generated explanation of its impact. Runs on your machine — nothing here is deployed to any cloud platform.

## Status

Early prototype: original development = 5 commits, all dated 2026-02-22 (README claims corrected 2026-10-06). Only the architecture below is implemented; everything in Roadmap is not.

## Architecture

- `main.py` — FastAPI app with a single `POST /decision` endpoint
- State is an in-memory dict (`fake_db`) keyed by `session_id`; it resets when the server restarts
- `google-generativeai` (`gemini-1.5-pro`) generates the `ai_response` text; requires the `GEMINI_API_KEY` env var, and the app refuses to start without it
- State updates are deterministic per decision: risk +10, financial impact +50000, public trust −5

## Roadmap (not implemented)

- [ ] Cloud Run deployment
- [ ] Gemini Live API voice interaction
- [ ] Firestore state persistence
- [ ] Vertex AI hosting

## Reproducible Testing

### 1. Create virtual environment
python -m venv venv

### 2. Activate environment (Windows)
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt google-generativeai

### 4. Set the API key (PowerShell)
$env:GEMINI_API_KEY = "your-key"

### 5. Run server
uvicorn main:app --reload

### 6. Test API
curl -X POST "http://127.0.0.1:8000/decision" -H "Content-Type: application/json" -d "{\"user_input\":\"option_a\"}"

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

## License

MIT — see [LICENSE](LICENSE).
