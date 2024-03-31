from pydantic import BaseModel


class TempValue(BaseModel):
    value: int


class TempWithDate(TempValue):
    date: str


class TempTableValue(TempWithDate):
    id: int
