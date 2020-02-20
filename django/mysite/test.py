from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(initial='name')
    url = forms.URLField(initial='http://')
    comment = forms.CharField()

data = {'name': '', 'url': '', 'comment': 'Foo'}

f = CommentForm(data)
