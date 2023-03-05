# urls.py 
from django.urls import path , include
from . import views

urlpatterns = [
path('',views.home),
path('products/',views.products),
path('customers/',views.customers),
]

