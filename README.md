# AI Crisis Simulator
Real-time multimodal AI crisis simulation platform powered by Gemini Live API and Google Cloud.
Enables leaders to stress-test high-stakes decisions through live voice interaction and persistent state tracking.

## Architecture
Client (Web / Voice UI)  
→ Cloud Run (FastAPI backend)  
→ Gemini Live API  
→ Firestore (state persistence)

## Reproducible Testing
git clone https://github.com/kswisse/ai-crisis-simulator.git
cd ai-crisis-simulator
pip install -r requirements.txt
uvicorn main:app --reload

