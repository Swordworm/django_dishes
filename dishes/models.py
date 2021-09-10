from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=20, unique=True)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='DishIngredient',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='OrderIngredient'
    )


class IngredientQuantity(models.Model):
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ]
    )

    class Meta:
        abstract = True


class DishIngredient(IngredientQuantity):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='dish_ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='dish_ingredients'
    )


class OrderIngredient(IngredientQuantity):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='order_ingredients'
    )
