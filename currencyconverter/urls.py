from django.urls import path
from . import views

app_name = "currencyconverter"

urlpatterns = [
    path('', views.converter, name='converter'),
]