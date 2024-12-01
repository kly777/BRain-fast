from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.card.card.crud import (
    create_card,
    delete_card,
    read_card,
    read_cards,
    update_card,
)
from api.public.card.card.models import CardCreate, CardRead, CardUpdate

router = APIRouter()


@router.post("", response_model=CardRead)
def create_a_card(card: CardCreate, db: Session = Depends(get_session)):
    return create_card(card=card, db=db)


@router.get("", response_model=list[CardRead])
def get_cards(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_cards(offset=offset, limit=limit, db=db)


@router.get("/{card_id}", response_model=CardRead)
def get_a_card(card_id: int, db: Session = Depends(get_session)):
    return read_card(card_id=card_id, db=db)


@router.patch("/{card_id}", response_model=CardRead)
def update_a_card(card_id: int, card: CardUpdate, db: Session = Depends(get_session)):
    return update_card(card_id=card_id, card=card, db=db)


@router.delete("/{card_id}")
def delete_a_card(card_id: int, db: Session = Depends(get_session)):
    return delete_card(card_id=card_id, db=db)