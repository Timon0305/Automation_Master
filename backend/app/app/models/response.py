from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base


class Response(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=False)
    fields = relationship("Field", secondary="responsefield")
    status_id = Column(Integer, ForeignKey("status.id"))
    status = relationship("Status", back_populates="responses")
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
