from django import forms
from .models import Newuser


class UserForm(forms.ModelForm):
    class Meta:
        model = Newuser
        fields = [
            'username',
            'email',
            'password',
            'remember_me'
        ]
class Createuser_Form(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    def clean_email(self, *rgs, **kwargs):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('this is an invalid email')
        return email

class ProductForm(forms.Form):
    product_category = forms.CharField(label='')
    Product_name = forms.CharField(label='')
    product_desc = forms.CharField(label='')
    product_price = forms.CharField(label='')