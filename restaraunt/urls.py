from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("contactus", views.contactus, name="contactus"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # ex: /polls/5/
   
]