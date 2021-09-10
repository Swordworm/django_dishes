from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import get_order_formset
from .models import Dish, DishIngredient, Order, OrderIngredient


def login_user(request, **kwargs):
    if request.user.is_authenticated:
        return redirect('dishes:index')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            return redirect('dishes:index')
        messages.info(request, 'incorrect login or password')
    return render(request, 'dishes/login.html', {'form': AuthenticationForm()})


def register_user(request):
    if request.user.is_authenticated:
        return redirect('dishes:index')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dishes:login')
    return render(request, 'dishes/register.html', {'form': form})


@login_required(login_url='dishes:login')
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("dishes:index")
    return render(request, "dishes/logout_confirm.html")


class DishesListView(ListView):
    model = Dish
    template_name = 'dishes/index.html'
    context_object_name = 'dishes'

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', 'created_at')
        return ordering

    def get_queryset(self):
        title = self.request.GET.get('q', '')
        object_list = self.model.objects.all()
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            object_list = object_list.order_by(*ordering)
        if title:
            object_list = object_list.filter(title__icontains=title)
        return object_list


class SingleDishView(DetailView):
    model = Dish
    template_name = 'dishes/single.html'
    context_object_name = 'dish'

    def get_queryset(self):
        return Dish.objects.prefetch_related('dish_ingredients__ingredient')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class OrderView(LoginRequiredMixin, View):
    login_url = '/login/'
    success_url = 'dishes/success.html'
    error_url = 'dishes/error.html'

    def get(self, request, *args, **kwargs):
        dish = Dish.objects.get(pk=kwargs.get('pk'))
        ingredients = dish.dish_ingredients.select_related('ingredient')
        OrderFormset = get_order_formset(
            extra=len(ingredients),
        )
        context = {
            'formset': OrderFormset(
                initial=[{'ingredient': item.ingredient, 'quantity': item.quantity} for item in ingredients],
                queryset=OrderIngredient.objects.none()
            ),
        }
        return render(request, 'dishes/order.html', context)

    def post(self, request, *args, **kwargs):
        dish = Dish.objects.get(pk=kwargs.get('pk'))
        ingredients = DishIngredient.objects.filter(dish=dish)
        OrderFormset = get_order_formset(
            extra=len(ingredients),
        )
        formset = OrderFormset(request.POST)
        if formset.is_valid() and request.user.is_authenticated:
            instances = formset.save(commit=False)
            order = Order.objects.create(dish_id=dish.id, user_id=request.user.id)
            for instance in instances:
                instance.order = order
            formset.save()
            return render(request, self.success_url)
        return render(request, self.error_url)


class OrdersListView(ListView):
    model = Order
    template_name = 'dishes/orders.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        orders = []
        for order in context['orders']:
            ingredients = order.order_ingredients.select_related('ingredient')
            orders.append({
                'order': order,
                'ingredients': [{'ingredient': item.ingredient, 'quantity': item.quantity} for item in ingredients]
            })
        context['orders'] = orders
        return context
