from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import schemas
import uuid

app = FastAPI(title="Mana Rythu AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/v1/health", response_model=schemas.HealthResponse)
def health():
    return schemas.HealthResponse(ok=True, version="0.1.0")

@app.post("/api/v1/query", response_model=schemas.QueryResponse)
def query(req: schemas.QueryRequest):
    # Stub implementation
    source = schemas.Source(id="doc1", title="Sample Document")
    return schemas.QueryResponse(
        answer_te="ఇది నమూనా సమాధానం.",
        answer_en="This is a sample answer.",
        sources=[source],
        confidence=0.8,
        tts_url=None,
    )

@app.post("/api/v1/image-diagnosis", response_model=schemas.ImageDiagnosisResponse)
def image_diagnosis(image: UploadFile = File(...)):
    # Stub model
    return schemas.ImageDiagnosisResponse(
        label="Leaf Blight",
        confidence=0.6,
        recommendation="Use appropriate fungicide.",
        precautions="Wear gloves while spraying."
    )

@app.post("/api/v1/escalate", response_model=schemas.EscalateResponse)
def escalate(req: schemas.EscalateRequest):
    ticket_id = str(uuid.uuid4())
    return schemas.EscalateResponse(ticketId=ticket_id, status="open")

@app.get("/api/v1/tickets", response_model=dict)
def tickets(status: str = "open", district: str | None = None):
    # Stub
    return {"items": []}

@app.patch("/api/v1/tickets/{ticket_id}", response_model=schemas.Ticket)
def update_ticket(ticket_id: str, req: schemas.Ticket):
    return req

@app.post("/api/v1/feedback", response_model=dict)
def feedback(req: schemas.FeedbackRequest):
    return {"ok": True}
