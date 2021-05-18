from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base


class Field(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    value = Column(JSON, nullable=False)
    responses = relationship("Response", secondary="responsefield")
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
