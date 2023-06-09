from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
def index(request):
        error = request.GET.get("errors")

        context = {"form":LoginForm(),"register":RegisterForm(),"errors":error}

        return render(request, "restaraunt/index.html", context)


def menu(request):
    menu_items=[
        {"name":"menu2_img_1.jpg","category":"Biryani","title":"Hyderabadi biryani","price":"$65.00"},
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
    context = {
    }
    return render(request, "restaraunt/contact.html", context)



def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('index')
            else:
                # Return an 'invalid login' error message
                error_message = 'Invalid login credentials'
                return redirect('/'+ f'?errors={error_message}')

            # return render(request, 'restaraunt/index.html',{'register':RegisterForm(),'errors':error_message,'form':LoginForm()})
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
            # return redirect('index')  # Replace 'login' with your desired URL for the login page
    else:
        register = RegisterForm()
        form = LoginForm()
    return render(request, 'restaraunt/index.html', {'register': RegisterForm(),'form':LoginForm()})

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('index')