from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.card import api as card_api


api = APIRouter()


api.include_router(
    card_api,
    prefix="/card",
    tags=["Card"],
    dependencies=[Depends(authent)],
)

