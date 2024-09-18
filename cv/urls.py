from django.urls import path

from polls.urls import app_name
from . import views

app_name = "cv"
urlpatterns = [
    path("", views.index, name="index"),
]