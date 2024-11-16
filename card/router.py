from typing import Optional
from fastapi import FastAPI, APIRouter, status
from .crud import *
from pydantic import BaseModel

router = APIRouter()
relation_router = APIRouter()


class CardIn(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


@router.get("/", status_code=status.HTTP_200_OK)
async def list_cards():
    cards = await r_cards()
    info = {
        "items": cards,
        "sum": len(cards)
    }
    return info


@router.get("/{card_id}", status_code=status.HTTP_200_OK)
async def read_card(card_id: int):
    card = await r_card(card_id)
    return card


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_card(card: CardIn):
    card = await c_card(card.title, card.content)
    return card


@router.put("/{card_id}", status_code=status.HTTP_200_OK)
async def update_card(card: CardIn):
    card = await u_card(card.title, card.content)


@router.delete("/{card_id}", status_code=status.HTTP_200_OK)
async def delete_card(card_id: int) -> None:
    card = await d_card(card_id)


@relation_router.get("/{relation_id}", status_code=status.HTTP_200_OK)
async def create_relation(relation_id: int):
    relation = await r_relation(relation_id)
    return relation


class RelationIn(BaseModel):
    relation: Optional[int] = None
    relata: Optional[int] = None


@relation_router.post("", status_code=status.HTTP_201_CREATED)
async def create_relation(relation: RelationIn):
    print(relation)
    relation = await c_relation(relation.relation, relation.relata)
    return relation

router.include_router(relation_router, prefix="/relation")
