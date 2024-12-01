from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from api.database import get_session
from api.public.card.relation.crud import (
    create_relation,
    delete_relation,
    read_relation,
    read_relations,
    update_relation,
)
from api.public.card.relation.models import RelationCreate, RelationRead, RelationUpdate,Relation
from api.utils.logger import logger_config

router = APIRouter()

logger = logger_config(__name__)


@router.post("", response_model=RelationRead)
def create_a_relation(relation: RelationCreate, db: Session = Depends(get_session)):
    logger.info("%s.create_a_relation: %s", __name__, relation)
    return create_relation(relation=relation, db=db)


@router.get("", response_model=list[RelationRead])
def get_relations(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    logger.info("%s.get_relations: triggered", __name__)
    return read_relations(offset=offset, limit=limit, db=db)


@router.get("/{relation_id}", response_model=RelationRead)
def get_a_relation(relation_id: int, db: Session = Depends(get_session)):
    logger.info("%s.get_a_relation.id: %s", __name__, relation_id)
    return read_relation(relation_id=relation_id, db=db)


@router.patch("/{relation_id}", response_model=RelationRead)
def update_a_relation(relation_id: int, relation: RelationUpdate, db: Session = Depends(get_session)):
    logger.info("%s.update_a_relation.id: %s", __name__, relation_id)
    return update_relation(relation_id=relation_id, relation=relation, db=db)


@router.delete("/{relation_id}")
def delete_a_relation(relation_id: int, db: Session = Depends(get_session)):
    logger.info("%s.delete_a_relation: %s triggered", __name__, relation_id)
    return delete_relation(relation_id=relation_id, db=db)