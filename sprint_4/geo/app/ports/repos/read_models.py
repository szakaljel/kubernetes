from tortoise.models import Model
from tortoise import fields


class City(Model):
    class Meta:
        table = "cities"

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    population = fields.IntField()
    time_zone = fields.CharField(max_length=50)

    def __str__(self):
        return self.name
