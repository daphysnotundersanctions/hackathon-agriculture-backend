
from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_plantInfo(
    plantInfo: _schemas.CreateContact, db: "Session"
) -> _schemas.Contact:
    plantInfo = _models.Contact(**plantInfo.dict())
    db.add(plantInfo)
    db.commit()
    db.refresh(plantInfo)
    return _schemas.Contact.from_orm(plantInfo)


async def get_all_plantInfo(db: "Session") -> List[_schemas.Contact]:
    plantInfo = db.query(_models.Contact).all()
    return list(map(_schemas.Contact.from_orm, plantInfo))


async def get_plantInfo(plantInfo_id: int, db: "Session"):
    plantInfo = db.query(_models.Contact).filter(_models.Contact.id == plantInfo_id).first()
    return plantInfo


async def delete_plantInfo(plantInfo: _models.Contact, db: "Session"):
    db.delete(plantInfo)
    db.commit()


async def update_plantInfo(
    plantInfo_data: _schemas.CreateContact, plantInfo: _models.Contact, db: "Session"
) -> _schemas.Contact:
    plantInfo.first_name = plantInfo_data.first_name
    plantInfo.last_name = plantInfo_data.last_name
    plantInfo.temperature = plantInfo_data.temperature
    plantInfo.humidity = plantInfo_data.humidity

    db.commit()
    db.refresh(plantInfo)

    return _schemas.Contact.from_orm(plantInfo)