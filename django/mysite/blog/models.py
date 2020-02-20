from django.db import models
from django import forms
from django.forms import ModelForm

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField(default='none')

    def __str__(self):
        return self.name

TITLE_CHOICES = {('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MS', 'Ms.')}
class Author(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline


