from tortoise.models import Model
from tortoise import fields


class Card(Model):
    id = fields.IntField(primary_key=True)
    title = fields.CharField(max_length=100)
    content = fields.TextField(blank=True)
    create_time = fields.DatetimeField(auto_now_add=True)
    modify_time = fields.DatetimeField(auto_now=True)
    priority = fields.IntField(default=0)

    def __str__(self):
        return self.title


class Relation(Model):
    relata = fields.ForeignKeyField(
        'card.Card', on_delete="CASCADE", related_name="as_relata")
    relation = fields.ForeignKeyField(
        'card.Card', on_delete="CASCADE", related_name='as_relation')
    position = fields.IntField(default=0)
    priority = fields.IntField(default=0)

    class Meta:
        unique_together = ('relata', 'relation', 'position')


class Tag(Model):
    tag = fields.ForeignKeyField(
        'card.Card', on_delete=fields.CASCADE, related_name='tags')
    card = fields.ForeignKeyField(
        'card.Card', on_delete=fields.CASCADE, related_name='cards')
    priority = fields.IntField(default=0)

    class Meta:
        unique_together = ('tag', 'card')

    def __str__(self):
        return self.tag.title
