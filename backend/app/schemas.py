from typing import List, Optional
from pydantic import BaseModel, Field

class Location(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None
    district: Optional[str] = None

class QueryRequest(BaseModel):
    text: Optional[str] = None
    audio: Optional[str] = None
    image_url: Optional[str] = None
    language: str
    location: Optional[Location] = None
    crop: Optional[str] = None
    stage: Optional[str] = Field(None, pattern="^(sowing|vegetative|flowering|harvest)$")
    userId: Optional[str] = None

class Source(BaseModel):
    id: str
    title: str

class QueryResponse(BaseModel):
    answer_te: str
    answer_en: str
    sources: List[Source]
    confidence: float
    tts_url: Optional[str] = None

class ImageDiagnosisResponse(BaseModel):
    label: str
    confidence: float
    recommendation: str
    precautions: str

class EscalateRequest(BaseModel):
    userId: str
    queryId: Optional[str] = None
    text: str
    attachments: Optional[List[str]] = None
    district: str
    suggested_answer: Optional[str] = None

class EscalateResponse(BaseModel):
    ticketId: str
    status: str

class Ticket(BaseModel):
    id: str
    user_id: str
    query_id: Optional[str]
    district: str
    text: str
    attachments_json: Optional[str]
    status: str
    officer_note: Optional[str]

class FeedbackRequest(BaseModel):
    queryId: str
    vote: str
    comment: Optional[str]

class HealthResponse(BaseModel):
    ok: bool
    version: str
