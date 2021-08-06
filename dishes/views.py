from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import DishForm
from .models import Dish


class DishesListView(View):
    def get(self, request):
        if request.GET.get('order') == 'desc':
            context = {"dishes": Dish.objects.all().order_by('-created')}
            return render(request, "dishes/index.html", context)
        context = {"dishes": Dish.objects.all()}
        return render(request, "dishes/index.html", context)


@method_decorator(csrf_exempt, name='dispatch')
class SingleDishView(DetailView):

    queryset = Dish.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        ingredients = []
        for dish_ingredient in self.object.dish_ingredients.all():
            ingredients.append(
                {
                    "id": dish_ingredient.id,
                    "name": dish_ingredient.ingredient,
                    "quantity": dish_ingredient.quantity,
                }
            )
        context['ingredients'] = ingredients
        return context

    def get(self, request, **kwargs):
        context = self.get_context_data()
        form = DishForm(ingredients=context['ingredients'])
        context['form'] = form
        return render(request, 'dishes/single.html', context)

    def post(self, request, **kwargs):
        form = DishForm(ingredients=request.POST)
        if form.is_valid():
            print(form)
        return render(request, 'dishes/thanks.html')
