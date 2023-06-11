from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict
from .models import Booking
from datetime import date
from datetime import datetime,timedelta

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100 ,  widget= forms.TextInput(attrs={"class":"mb_30"}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"mb_30"}))

class RegisterForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes to specific fields
        self.fields['username'].widget.attrs['class'] = 'mb_20'
        self.fields['email'].widget.attrs['class'] = 'mb_20'
        self.fields['password1'].widget.attrs['class'] = 'mb_20'
        self.fields['password2'].widget.attrs['class'] = 'mb_20'
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields= '__all__'
        exclude=['owner','table']
        widgets={
            'date':forms.DateInput(attrs={'type':'date', 'min': date.today().strftime('%Y-%m-%d'),'class':'form-control mb_15'}),
            # 'time':forms.TimeInput(attrs={'type':'time','min': (datetime.now() - timedelta(minutes=5)).strftime('%H:%M')})
            'time':forms.TimeInput(attrs={'type':'time','class':'form-control mb_15'})
        }