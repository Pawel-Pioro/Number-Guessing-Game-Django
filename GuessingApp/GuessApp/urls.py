from django.urls import path
from . import views

app_name = "GuessApp"

urlpatterns = [
    path("", views.indexView.as_view(), name="index"),
]