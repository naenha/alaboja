from django.urls import path
from .views import myhome, aboutus, store

app_name = "alaboja"
urlpatterns = [
    path('myhome/', myhome, name="myhome"),
    path('aboutus/', aboutus, name="aboutus"),
    path('store/', store, name="store"),
]

