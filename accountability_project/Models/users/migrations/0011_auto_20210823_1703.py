# Generated by Django 3.1.8 on 2021-08-23 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210728_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='score_board',
        ),
        migrations.RemoveField(
            model_name='user',
            name='score_board',
        ),
    ]
