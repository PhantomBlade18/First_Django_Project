# Generated by Django 3.1.1 on 2020-10-29 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20201027_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='age',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='shows',
        ),
        migrations.RemoveField(
            model_name='show',
            name='description',
        ),
        migrations.RemoveField(
            model_name='show',
            name='rating',
        ),
    ]
