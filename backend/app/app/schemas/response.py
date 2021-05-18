from pydantic import BaseModel

from .status import Status
from datetime import datetime


# Shared properties
class ResponseBase(BaseModel):
    name: str = None
    description: str = None
    status: Status = None


# Properties to receive on response creation
class ResponseCreate(ResponseBase):
    pass


# Properties to receive on response update
class ResponseUpdate(ResponseBase):
    pass


# Properties shared by models stored in DB
class ResponseInDBBase(ResponseBase):
    id: int
    name: str
    description: str
    status_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Response(ResponseInDBBase):
    pass


# Properties properties stored in DB
class ResponseInDB(ResponseInDBBase):
    pass
