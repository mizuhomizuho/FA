from fastapi import FastAPI
from contextlib import asynccontextmanager
from urllib.request import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from starlette import status
from starlette.responses import JSONResponse
from lib.items.router import router as items_router
from lib.lib import Lib

@asynccontextmanager
async def lifespan(app: FastAPI):
    inst = Lib('tools/tools', 'Tools').get()()
    await inst.lifespan()
    yield
    await inst.lifespan_end()

app = FastAPI(lifespan=lifespan, title='FAProj')

@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({'meow': True, 'detail': exc.errors()})
    )

app.include_router(items_router)

@app.get('/')
async def hi():
    return {'data': 'Hi'}
