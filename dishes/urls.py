from django.urls import path

from . import views

app_name = "dishes"

urlpatterns = [
    path('', views.DishesListView.as_view(), name='index'),
    path('<int:pk>/', views.SingleDishView.as_view(), name='single_dish'),
    path('<int:pk>/order', views.OrderView.as_view(), name='order'),
    path('orders/', views.OrdersListView.as_view(), name='orders'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
]
