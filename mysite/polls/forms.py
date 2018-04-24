from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PUser

class AddressMixin(forms.ModelForm):
    class Meta:
        model = PUser
        fields = ('city',)
        widgets = {
            'city': forms.TextInput(attrs={'class':'form-control'}),
        }

class UsersForm(AddressMixin):
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
    )