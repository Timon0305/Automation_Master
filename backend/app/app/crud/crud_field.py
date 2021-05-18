from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.field import Field
from app.schemas.field import FieldCreate, FieldUpdate
from app.crud.base import CRUDBase


class CRUDField(CRUDBase[Field, FieldCreate, FieldUpdate]):
    def create_field(self, db_session: Session, *, obj_in: FieldCreate) -> Field:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj

    def get_multi_by_response(
        self, db_session: Session, *, response_id: int, skip=0, limit=100
    ) -> List[Field]:
        return (
            db_session.query(self.model)
            .filter(Field.response_id == response_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


field = CRUDField(Field)
