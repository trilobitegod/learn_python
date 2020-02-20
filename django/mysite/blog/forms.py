from django import forms
from django.forms import ModelForm, Textarea
from .models import Blog, Author


BIRTH_YEAR_CHOICE = {'1980', '1981', '1982'}
class NameForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'special'}))
    message = forms.CharField(widget=forms.Textarea)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICE))

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows':20}),
        }