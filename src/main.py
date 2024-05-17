import datetime
from sqlalchemy import select
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_async_session
from .temp.modeles import TempTable, temp
from .temp.shemas import TempValue, TempTableValue

app = FastAPI(
    title="ARDUINO TEST"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/temp')
async def put_temp(meteo_value: TempValue, db: AsyncSession = Depends(get_async_session)):
    tempTable = TempTable(temp_value=meteo_value.value, date=str(datetime.datetime.now()))
    db.add(tempTable)
    await db.commit()
    await db.refresh(tempTable)

    return {"result": "ВСЕ ХОРОШО!"}


@app.get('/now/temp')
async def get_temp(db: AsyncSession = Depends(get_async_session)):
    temp_value = await db.execute(select(temp).order_by(temp.c.id.desc()).limit(1))
    result = temp_value.all().__getitem__(0)
    converted_res = TempTableValue(id=result.id, value=result.temp_value, date=result.date)
    # SELECT * FROM item ORDER BY id DESC LIMIT 1
    return converted_res


@app.post('/temp/list')
async def get_list_temp(db: AsyncSession = Depends(get_async_session)):
    temp_value = await db.execute(select(temp).order_by(temp.c.date.desc()).limit(5))
    result = temp_value.all()
    converted_res = []
    for i in range(0, 5):
        converted_res.append(TempTableValue(id=result.__getitem__(i).id, value=result.__getitem__(i).temp_value, date=result.__getitem__(i).date))
    return converted_res
