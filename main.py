from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.concurrency import asynccontextmanager
from card.router import router as card_router
from card.router import relation_router as relation_router
from orm import init_db, close_db
from asyncio.exceptions import CancelledError


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("init_db")
    yield
    await close_db()

app = FastAPI(lifespan=lifespan)
app.include_router(card_router, prefix="/card")




@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"message": f"HTTP error: {exc.detail}"}


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return {"message": "An unexpected error occurred"}


@app.middleware("http")
async def catch_cancelled_error(request: Request, call_next):
    try:
        response = await call_next(request)
    except CancelledError:
        return {"message": "Request was cancelled"}
    return response


@app.exception_handler(CancelledError)
async def handle_cancelled_error(request, exc):
    return {"message": "Request was cancelled"}
