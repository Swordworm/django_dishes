from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Dish(models.Model):
    title = models.CharField(max_length=20)
    ingredients = models.ManyToManyField(
        'Ingredient',
        through='DishIngredient',
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ['created']

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)


class DishIngredient(models.Model):
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='dish_ingredients'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ]
    )


class OrderDish(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_dish'
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ]
    )