# Generated by Django 3.0.3 on 2020-02-20 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_confirmstring'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]