from django.urls import path
from .views import myhome, aboutus

app_name = "alaboja"
urlpatterns = [
    path('myhome/', myhome, name="myhome"),
    path('aboutus/', aboutus, name="aboutus"),
]

