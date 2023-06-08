from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
    }
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