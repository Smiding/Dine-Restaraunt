from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm, BookingForm
from django.core.exceptions import ValidationError
# , BookingForm
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Booking
from .mixins import AdminRequiredMixin,UserorAdminRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect('booking_list')
        elif request.user.is_authenticated:
            return redirect('booking_list')
            
        error = request.GET.get("errors")

        context = {"form":LoginForm(),"register":RegisterForm(),"errors":error}

        return render(request, "restaraunt/index.html", context)


def menu(request):
    menu_items=[
        {"name":"menu2_img_1.jpg","category":"Biryani","title":"Hyderabadi","price":"$65.00"},
        {"name":"menu2_img_2.jpg","category":"Chicken","title":"Daria Shevtsova","price":"$80.00"},
        {"name":"menu2_img_3.jpg","category":"Burger","title":"Spicy Burger","price":"$100.00"},
        {"name":"menu2_img_4.jpg","category":"Dessert","title":"Fried Chicken","price":"$99.00"},
        {"name":"menu2_img_5.jpg","category":"kabab","title":"Mozzarella Sticks","price":"$75.00"},
        {"name":"menu2_img_6.jpg","category":"kacchi","title":"Popcorn Chicken","price":"$65.00"},
        {"name":"menu2_img_7.jpg","category":"noodles","title":"Chicken Wings","price":"$79.00"},
        {"name":"menu2_img_8.jpg","category":"grill","title":"Onion Rings","price":"$110.00"},
        
        ]
    context = {"items":menu_items
    }
    return render(request, "restaraunt/menu.html", context)

def contactus(request):

    return render(request, "restaraunt/contact.html",)



def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = 'Invalid login credentials'
                return redirect('/'+ f'?errors={error_message}')
    else:
        return redirect('index')


def register(request):
    if request.method == 'GET':
        return redirect('index')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'restaraunt/index.html',{'register':RegisterForm(),'errors':form.errors,'form':LoginForm()})
    else:
        register = RegisterForm()
        form = LoginForm()
    return render(request, 'restaraunt/index.html', {'register': RegisterForm(),'form':LoginForm()})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')
    

class BookingListView(LoginRequiredMixin,ListView):
    model = Booking
    template_name = 'restaraunt/booking.html'
    context_object_name = 'bookings'  
    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(owner=self.request.user)


class BookingCreateView(LoginRequiredMixin,CreateView):
    model = Booking
    template_name = 'restaraunt/booking_create.html'
    success_url = reverse_lazy('booking_list')
    form_class=BookingForm

    def form_valid(self, form):
        try:
            form.instance.owner=self.request.user
            form.is_valid()
            response= super().form_valid(form)  # Call the parent class method to save the form
            return response
        except ValidationError as e:
            error_message = ', '.join(e.messages)
            context = {"errors":error_message,"form":BookingForm(initial={'owner':self.request.user})}

        return render(self.request, "restaraunt/booking_create.html", context)


class BookingUpdateView(UpdateView,AdminRequiredMixin):
    model = Booking
    template_name = 'restaraunt/booking.html'
    fields = ['Name', 'Capacity', 'status']
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView,AdminRequiredMixin):
    model = Booking
    template_name = 'restaraunt/confirm_delete.html'
    success_url = reverse_lazy('booking_list')