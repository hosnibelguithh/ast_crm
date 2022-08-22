from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser





class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    Admin = forms.BooleanField()
    Agent = forms.BooleanField()
    

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2','phonenumber','Admin', 'Agent')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Pseudonyme"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"
        self.fields['password2'].help_text = "Entrez le même mot de passe, pour vérification"
        self.fields['phonenumber'].label = "Numéro de teléphone"


       
class CustomUserChangeCreationForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phonenumber = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    Admin = forms.BooleanField()
    Agent = forms.BooleanField()
    

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2','phonenumber','Admin', 'Agent')
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Pseudonyme"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"
        self.fields['password2'].help_text = "Entrez le même mot de passe, pour vérification"
        self.fields['phonenumber'].label = "Numéro de teléphone"


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'phonenumber',
        ]