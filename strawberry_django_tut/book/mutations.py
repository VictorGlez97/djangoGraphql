import typing
import strawberry 
import strawberry_django 
from strawberry import auto
from . import models

# TIPO DE SALIDA PARA FRUIT
@strawberry_django.type(models.Fruit)
class iFruit:
    id: auto
    name: auto 
    color: 'iColor'

# TIPO DE SALIDA PARA COLOR
@strawberry_django.type(models.Color)
class iColor:
    id: auto 
    name: auto 
    fruits: typing.List[iFruit]

# MUTACIONES COLOR
@strawberry.type
class ColorMutation:
    @strawberry.mutation
    def create_color(self, name: str) -> iColor:
        print(name)
        color = models.Color(name=name)
        color.save()
        return True
    
# # MUTACIONES FRUTA
# @strawberry.type
# class FruitMutation:
#     @strawberry.mutation
#     def create_fruit(self, name: str, color_id: int) -> Fruit:
#         color = models.Color.objects.get(id=color_id)

#         fruit = models.Fruit(name=name, color=color)
#         fruit.save()

#         return fruit