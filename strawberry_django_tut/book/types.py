import typing
from django.db import models

# import strawberry_django
# from strawberry import auto

from . import models
import strawberry

# @strawberry.django.type(models.Fruit)
# class Fruit:
#     id: typing.auto
#     name: typing.auto
#     color: 'Color'

@strawberry.input
class FruitInput:
    name: typing.Optional[str] = None
    color: typing.Optional[int] = None

# @strawberry.django.type(models.Color)
# class Color:
#     id: strawberry.auto
#     name: strawberry.auto
#     fruits: typing.List[Fruit]

@strawberry.input
class ColorInput:
    name: typing.Optional[str]