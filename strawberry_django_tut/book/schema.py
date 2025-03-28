import typing
import strawberry 
import strawberry.django
import strawberry_django 
from strawberry_django.optimizer import DjangoOptimizerExtension

from .types import Fruit, Color
from .mutations import ColorMutation#, FruitMutation

@strawberry.type
class Query:
    fruits: typing.List[Fruit] = strawberry_django.field()
    colors: typing.List[Color] = strawberry_django.field()

@strawberry.type
class Mutation: 
    create_color: ColorMutation = strawberry.field(resolver=ColorMutation.create_color)
#     create_fruit: FruitMutation = strawberry.field(resolver=FruitMutation.create_fruit)

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ]
)