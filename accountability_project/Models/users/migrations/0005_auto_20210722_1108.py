# Generated by Django 3.1.8 on 2021-07-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210722_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
