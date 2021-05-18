from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Status(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    value = Column(String, nullable=False, unique=True, index=True)
    responses = relationship("Response", back_populates="status")
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
