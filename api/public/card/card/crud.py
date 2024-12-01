from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from api.database import get_session
from api.public.card.card.models import Card, CardCreate, CardUpdate


def create_card(card: CardCreate, db: Session = Depends(get_session)):
    card_to_db = Card.model_validate(card)
    db.add(card_to_db)
    db.commit()
    db.refresh(card_to_db)
    return card_to_db


def read_cards(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    cards = db.exec(select(Card).offset(offset).limit(limit)).all()
    return cards


def read_card(card_id: int, db: Session = Depends(get_session)):
    card = db.get(Card, card_id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card not found with id: {card_id}",
        )
    return card


def update_card(card_id: int, card: CardUpdate, db: Session = Depends(get_session)):
    card_to_update = db.get(Card, card_id)
    if not card_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card not found with id: {card_id}",
        )

    card_data = card.model_dump(exclude_unset=True)
    for key, value in card_data.items():
        setattr(card_to_update, key, value)

    db.add(card_to_update)
    db.commit()
    db.refresh(card_to_update)
    return card_to_update


def delete_card(card_id: int, db: Session = Depends(get_session)):
    card = db.get(Card, card_id)
    if not card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card not found with id: {card_id}",
        )

    db.delete(card)
    db.commit()
    return {"ok": True}
