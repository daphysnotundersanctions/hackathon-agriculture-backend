import datetime as _dt
import pydantic as _pydantic


class _BaseContact(_pydantic.BaseModel):
    first_name: str
    last_name: str
    temperature: str
    humidity: str


class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class CreateContact(_BaseContact):
    pass