from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from ..relation.models import Relation


class CardBase(SQLModel):
    name: str
    description: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Card 1",
                "description": "This is card 1",
            }
        }


class Card(CardBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # relations: list["Relation"] = Relationship(back_populates="related_card")
    relatas: list["Relation"] = Relationship(back_populates="relata",link_model="Relation")
    relations: List["Relation"] = Relationship(back_populates="relation",link_model="Relation")

class CardCreate(CardBase):
    pass


class CardRead(CardBase):
    id: int
    name: str | None = None
    description: str | None = None
    # relations: list["Relation"] = []
    # relatas: list["Relation"] = []


class CardUpdate(CardBase):
    name: str | None = None
    description: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Card 1",
                "description": "This is card 1",
            }
        }
