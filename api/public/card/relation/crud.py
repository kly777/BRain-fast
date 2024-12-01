from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select, text

from api.database import get_session
from api.public.card.relation.models import Relation, RelationCreate, RelationUpdate
from api.public.card.card.models import Card


def create_relation(relation: RelationCreate, db: Session = Depends(get_session)):
    # 检查 relation_id 和 relata_id 对应的 Card 是否存在
    relation_card = db.get(Card, relation.relation_id)
    if not relation_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card not found with id: {relation.relation_id}",
        )

    relata_card = db.get(Card, relation.relata_id)
    if not relata_card:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Card not found with id: {relation.relata_id}",
        )

    # 创建 Relation 对象
    relation_to_db = Relation.from_orm(relation)
    db.add(relation_to_db)
    db.commit()
    db.refresh(relation_to_db)
    return relation_to_db


def read_relations(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    relations = db.exec(select(Relation).offset(offset).limit(limit)).all()
    return relations


def read_relation(relation_id: int, db: Session = Depends(get_session)):
    relation = db.get(Relation, relation_id)
    if not relation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Relation not found with id: {relation_id}",
        )
    return relation


def update_relation(relation_id: int, relation: RelationUpdate, db: Session = Depends(get_session)):
    relation_to_update = db.get(Relation, relation_id)
    if not relation_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Relation not found with id: {relation_id}",
        )

    relation_data = relation.dict(exclude_unset=True)
    for key, value in relation_data.items():
        setattr(relation_to_update, key, value)

    db.add(relation_to_update)
    db.commit()
    db.refresh(relation_to_update)
    return relation_to_update


def delete_relation(relation_id: int, db: Session = Depends(get_session)):
    relation = db.get(Relation, relation_id)
    if not relation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Relation not found with id: {relation_id}",
        )

    db.delete(relation)
    db.commit()
    return {"ok": True}
