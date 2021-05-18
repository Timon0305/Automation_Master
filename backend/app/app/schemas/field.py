from datetime import datetime

from pydantic import BaseModel


# Shared properties
class FieldBase(BaseModel):
    name: str = None
    value: str = None


# Properties to receive on field creation
class FieldCreate(FieldBase):
    pass


# Properties to receive on field update
class FieldUpdate(FieldBase):
    pass


# Properties shared by models stored in DB
class FieldInDBBase(FieldBase):
    id: int
    name: str
    response_id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Field(FieldInDBBase):
    pass


# Properties properties stored in DB
class FieldInDB(FieldInDBBase):
    pass
