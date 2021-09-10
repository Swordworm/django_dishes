from django.contrib import admin

from .models import Ingredient, Dish, Order


class DishIngredientInline(
    admin.TabularInline
):
    model = Dish.ingredients.through


class DishAdmin(
    admin.ModelAdmin
):
    list_display = ('title', 'created_at')
    inlines = [
        DishIngredientInline
    ]


admin.site.register(Ingredient)
admin.site.register(Order)
admin.site.register(Dish, DishAdmin)
