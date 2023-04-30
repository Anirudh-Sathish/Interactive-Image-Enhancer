from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("output/", views.output, name="output"),
    path("output2/", views.output2, name="output2"),
]
