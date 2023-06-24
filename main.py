from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/plantInfo/", response_model=_schemas.Contact)
async def create_plantInfo(
    plantInfo: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_plantInfo(plantInfo=plantInfo, db=db)


@app.get("/api/plantInfo/", response_model=List[_schemas.Contact])
async def get_plantInfo(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_plantInfo(db=db)


@app.get("/api/plantInfo/{plantInfo_id}/", response_model=_schemas.Contact)
async def get_plantInfo(
    plantInfo_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    plantInfo = await _services.get_plantInfo(db=db, plantInfo_id=plantInfo_id)
    if plantInfo is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    return plantInfo


@app.delete("/api/plantInfos/{plantInfo_id}/")
async def delete_plantInfo(
    plantInfo_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    plantInfo = await _services.get_plantInfo(db=db, plantInfo_id=plantInfo_id)
    if plantInfo is None:
        raise _fastapi.HTTPException(status_code=404, detail="plantInfo does not exist")

    await _services.delete_plantInfo(plantInfo, db=db)

    return "successfully deleted the user"


@app.put("/api/plantInfo/{plantInfo_id}/", response_model=_schemas.Contact)
async def update_plantInfo(
    plantInfo_id: int,
    plantInfo_data: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    plantInfo = await _services.get_plantInfo(db=db, plantInfo_id=plantInfo_id)
    if plantInfo is None:
        raise _fastapi.HTTPException(status_code=404, detail="plantInfo does not exist")

    return await _services.update_plantInfo(
        plantInfo_data=plantInfo_data, plantInfo=plantInfo, db=db
    )