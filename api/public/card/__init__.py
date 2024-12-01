from fastapi import APIRouter, Depends

from api.auth import authent
from api.public.card.card import views as card
from .relation import views as relation
# from api.public.card.relation import views as heroes
# from api.public.card.group import views as teams

api = APIRouter()


api.include_router(
    card.router,
    prefix="/card",
    tags=["Card"],
    dependencies=[Depends(authent)],
)

api.include_router(
    relation.router,
    prefix="/relation",
    tags=["Relation"],
    dependencies=[Depends(authent)],
)