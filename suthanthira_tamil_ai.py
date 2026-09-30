from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="சுதந்திர தமிழ் AI")

class AnalysisRequest(BaseModel):
    query: str

@app.post("/analyze")
def analyze_data(request: AnalysisRequest):
    try:
        query = request.query.lower()
        if "capital of india" in query:
            answer = "New Delhi"
        else:
            answer = "Sorry, I can only answer about the capital of India for now."
            
        return {"status": "Analysis completed", "result": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
