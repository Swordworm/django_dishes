from django.contrib import admin

from .models import Ingredient, Dish


class DishIngredientInline(
    admin.TabularInline
):
    model = Dish.ingredients.through


class DishAdmin(
    admin.ModelAdmin
):
    list_display = ('title', 'created')
    inlines = [
        DishIngredientInline
    ]


admin.site.register(Ingredient)
admin.site.register(Dish, DishAdmin)
