from pydantic import BaseModel

from datetime import datetime


# Shared properties
class StatusBase(BaseModel):
    name: str = None
    value: str = None


# Properties to receive on status creation
class StatusCreate(StatusBase):
    pass


# Properties to receive on status update
class StatusUpdate(StatusBase):
    pass


# Properties shared by models stored in DB
class StatusInDBBase(StatusBase):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Status(StatusInDBBase):
    pass


# Properties properties stored in DB
class StatusInDB(StatusInDBBase):
    pass
