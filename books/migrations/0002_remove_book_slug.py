# Generated by Django 3.2.7 on 2022-06-03 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
    ]
