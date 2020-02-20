from django.db import models


class Students(models.Model):
    def __str__(self):
        return self.year_in_school
    FRESHMEN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JU'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMEN, 'Freshmen'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMEN,
    )


class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person)
    def __str__(self):
        return self.name
