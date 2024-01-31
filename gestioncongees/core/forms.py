from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import CustomUser
from django.contrib.auth.models import User


INPUT_CLASSES = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class LoginForm(AuthenticationForm):

        username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class' : 'w-full py-4 px-6 rounded-xl'
        }))
        
        password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class' : 'w-full py-4 px-6 rounded-xl'
        }))



class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','password1', 'password2','sold','role')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class' : INPUT_CLASSES
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class' : INPUT_CLASSES
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class' : INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email @',
        'class' : INPUT_CLASSES
    }))

    # photo = forms.FileInput(attrs={
    #     'class': INPUT_CLASSES
    # }),

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class' : INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class' : INPUT_CLASSES
    }))

    sold = forms.IntegerField( show_hidden_initial=True,initial=24)
     
    role = forms.CharField(initial='user', show_hidden_initial=True)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class' : INPUT_CLASSES
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class' : INPUT_CLASSES
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class' : INPUT_CLASSES
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email @',
        'class' : INPUT_CLASSES
    }))

    # photo = forms.FileInput(attrs={
    #     'class': INPUT_CLASSES
    # }),

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class' : INPUT_CLASSES
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class' : INPUT_CLASSES
    }))