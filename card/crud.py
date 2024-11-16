from fastapi import HTTPException
from .models import Card, Relation
from tortoise.exceptions import DoesNotExist
from fastapi.exceptions import ValidationException


async def r_cards():
    cards = await Card.all()
    return cards


async def c_card(title, content):
    card = await Card.create(title=title, content=content)
    return card


async def r_card(id):
    try:
        card = await Card.get(id=id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


async def u_card(id, title, content):
    card = await Card.filter(id=id).update(title=title, content=content)
    return card


async def d_card(id):
    try:
        card = await Card.get(id=id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Card not found")
    await card.delete()
    return {"message": "Card deleted successfully"}

async def r_relation(id):
    relation = await Relation.get(id=id)
    return relation

async def c_relation(relation_id,relata_id):
    relation = await Relation.create(relation=relation_id, relata=relata_id)
    return relation
