from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("contactus", views.contactus, name="contactus"),
    # ex: /polls/5/
   
]