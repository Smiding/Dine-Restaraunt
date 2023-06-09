from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from collections import OrderedDict

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100 ,  widget= forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields = ['username','email','password1','password2']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields = OrderedDict(self.fields)
            for field_name, field in self.fields.items():
                self.fields[field_name].widget.attrs['placeholder'] = field.label