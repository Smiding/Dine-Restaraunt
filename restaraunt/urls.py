from django.urls import path
from django.contrib.auth.views import LogoutView



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
]
#     # Tables
urlpatterns += [
    path('booking/', views.BookingListView.as_view(), name='booking_list'),
    path('booking_create/', views.BookingCreateView.as_view(), name='booking_create'),

    path('booking/delete/<int:pk>/', views.BookingDeleteView.as_view(), name='booking_delete'),
]  
