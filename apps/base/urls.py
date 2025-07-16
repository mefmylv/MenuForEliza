from django.urls import path
from .views import *

urlpatterns = [
    path('reservation/', reservation, name="reservation"),
    path('menu/', menu_food, name="menu_food"),
    path('about/', about_us, name='about'),
    path('', home, name='homepage'),
    path('reservation/submit/', reservation_submit, name='reservation_submit'), 
]