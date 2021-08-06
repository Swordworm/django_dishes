from django.urls import path

from . import views


app_name = "dishes"

urlpatterns = [
    path("", views.DishesListView.as_view(), name="index"),
    path("<int:pk>/", views.SingleDishView.as_view(), name="single_dish"),
    # path("<int:pk>/", views.PostDetailView.as_view(), name="details"),
]
