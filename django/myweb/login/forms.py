from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(max_length=128, label='User name', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Username", 'autofocus': ''}))
    password = forms.CharField(max_length=256, label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Password"}))
    captcha = CaptchaField(label='Captcha')


class RegisterForm(forms.Form):
    gender = (('male',"男"), ('female',"女"))
    username = forms.CharField(max_length=128, label="User name", widget=forms.TextInput(
        attrs={'class': 'forms-control'}))
    password1 = forms.CharField(max_length=256, label="Password", widget=forms.PasswordInput(
        attrs={'class': 'forms-control'}))
    password2 = forms.CharField(max_length=256, label="Password Again", widget=forms.PasswordInput(
        attrs={'class': 'forms-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'forms-control'}))
    sex = forms.ChoiceField(choices=gender)
    captcha = CaptchaField(label='Captcha')