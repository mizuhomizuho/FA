from contextlib import asynccontextmanager
from fastapi import FastAPI
from router import router as items_router
# from db import create_db, drop_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await drop_db()
    # print('Drop db')
    # await create_db()
    # print('Create db')
    yield
    print('End')

app = FastAPI(lifespan=lifespan)
app.include_router(items_router)

@app.get('/')
async def hi():
    return {'data': 'Hi1'}
