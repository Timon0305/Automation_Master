from sqlalchemy import Column, ForeignKey, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base


class Action(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, index=True)
    data = Column(JSON)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User")
    response_id = Column(Integer, ForeignKey("response.id"))
    response = relationship("Response")
