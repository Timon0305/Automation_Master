from sqlalchemy import Column, ForeignKey, Integer, DateTime
from datetime import datetime
from app.db.base_class import Base


class ResponseField(Base):
    response_id = Column(Integer, ForeignKey("response.id"), primary_key=True)
    field_id = Column(Integer, ForeignKey("field.id"), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
