from django.db import models
from typing import Optional
import strawberry

class Fruit(models.Model):
    name = models.CharField(max_length=20)
    color = models.ForeignKey(
        "Color",
        on_delete=models.CASCADE,
        related_name="fruits",
        blank=True,
        null=True
    )

@strawberry.input
class FruitInput:
    name: Optional[str] = None
    color: Optional[int] = None

class Color(models.Model):
    name = models.CharField(max_length=20, help_text='field description')

@strawberry.input
class ColorInput:
    name: Optional[str]