from fastapi import FastAPI
from contextlib import asynccontextmanager
from lib.items.router import router as items_router
from lib.lib import Lib


@asynccontextmanager
async def lifespan(app: FastAPI):
    inst = Lib('tools/tools', 'Tools').get()()
    await inst.lifespan()
    yield
    await inst.lifespan_end()

app = FastAPI(lifespan=lifespan)

app.include_router(items_router)

@app.get('/')
async def hi():
    return {'data': 'Hi'}
