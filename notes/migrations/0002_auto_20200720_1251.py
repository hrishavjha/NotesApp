# Generated by Django 3.0.8 on 2020-07-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='date_of_creation',
            field=models.DateTimeField(auto_now=True),
        ),
    ]