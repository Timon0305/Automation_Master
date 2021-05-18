from datetime import datetime

from pydantic import BaseModel

from .field import Field
from .response import Response


# Shared properties
class ResponseFieldBase(BaseModel):
    response: Response
    field: Field


# Properties to receive on responsefield creation
class ResponseFieldCreate(ResponseFieldBase):
    pass


# Properties to receive on responsefield update
class ResponseFieldUpdate(ResponseFieldBase):
    pass


# Properties shared by models stored in DB
class ResponseFieldInDBBase(ResponseFieldBase):
    response_id: int
    field_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class ResponseField(ResponseFieldInDBBase):
    pass


# Properties properties stored in DB
class ResponseFieldInDB(ResponseFieldInDBBase):
    pass
