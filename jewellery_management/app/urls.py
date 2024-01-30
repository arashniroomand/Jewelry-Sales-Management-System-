from django.urls import path
from .views import *

urlpatterns = [
    path('jewellery', JewelleryView, name="JewelleryView")
]
