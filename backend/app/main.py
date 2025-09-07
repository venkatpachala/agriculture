from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import schemas
from adapters.llm import LLMClient
from adapters.stt import transcribe
from adapters.tts import synthesize
from adapters.cv import classify
from rag import retriever
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
    text = req.text
    if req.audio:
        try:
            text = transcribe(req.audio)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid audio")
    if not text:
        raise HTTPException(status_code=400, detail="No query text provided")

    try:
        retrieved = retriever.retrieve(text)
    except Exception:
        retrieved = []
    sources = [
        schemas.Source(id=str(i), title=doc[:50])
        for i, (_, doc) in enumerate(retrieved)
    ]

    llm = LLMClient()
    answer_en = llm.generate(text)
    answer_te = answer_en  # Stub translation
    tts_url = synthesize(answer_te)

    return schemas.QueryResponse(
        answer_te=answer_te,
        answer_en=answer_en,
        sources=sources,
        confidence=0.8,
        tts_url=tts_url,
    )

@app.post("/api/v1/image-diagnosis", response_model=schemas.ImageDiagnosisResponse)
def image_diagnosis(image: UploadFile = File(...)):
    image_bytes = image.file.read()
    label, confidence = classify(image_bytes)
    recommendation = "Monitor crop" if label == "healthy" else "Apply treatment"
    precautions = "Wear gloves" if label != "healthy" else "None"
    return schemas.ImageDiagnosisResponse(
        label=label,
        confidence=confidence,
        recommendation=recommendation,
        precautions=precautions,
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
