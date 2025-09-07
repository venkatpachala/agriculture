from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True)
    name = Column(String)
    district = Column(String)
    language = Column(String, default='te')
    created_at = Column(DateTime, default=datetime.utcnow)

class Query(Base):
    __tablename__ = 'queries'
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    text = Column(Text)
    language = Column(String)
    crop = Column(String)
    stage = Column(String)
    location_json = Column(Text)
    answer_te = Column(Text)
    answer_en = Column(Text)
    sources_json = Column(Text)
    confidence = Column(Float)
    latency_ms = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(String, index=True)
    vote = Column(String)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    query_id = Column(String, index=True, nullable=True)
    district = Column(String)
    text = Column(Text)
    attachments_json = Column(Text)
    status = Column(String, default='open')
    officer_note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Document(Base):
    __tablename__ = 'documents'
    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    embedding = Column(Text)
    tags_json = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
