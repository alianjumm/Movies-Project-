# Generated by Django 4.0.3 on 2022-03-31 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='main_app.actor'),
        ),
    ]
