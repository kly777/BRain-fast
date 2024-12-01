from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..card.models import Card

class RelationBase(SQLModel):
    relation_id: Optional[int] = Field(default=None, foreign_key="card.id")
    relata_id: Optional[int] = Field(default=None, foreign_key="card.id")
    relation: "Card" = Relationship(back_populates="relations",sa_relationship=relationship('Thing', foreign_keys=relation_id))
    relata: "Card" = Relationship(back_populates="relatas",sa_relationship=relationship('Thing', foreign_keys=relata_id))
    
class Relation(RelationBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class RelationCreate(RelationBase):
    pass

class RelationRead(RelationBase):
    id: int

class RelationUpdate(RelationBase):
    pass
