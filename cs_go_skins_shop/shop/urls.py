from django.urls import path
from .views import *

urlpatterns = [
    path('', shopHome, name='home'),
    path('shop/', shopShop, name='shop'),
    path('about/', shopAbout, name='about'),
    path('contact/', shopContact, name='contact'),
]