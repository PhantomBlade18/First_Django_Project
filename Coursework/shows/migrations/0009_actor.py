# Generated by Django 3.1.1 on 2020-10-29 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_delete_actor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=50)),
                ('actor_age', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
