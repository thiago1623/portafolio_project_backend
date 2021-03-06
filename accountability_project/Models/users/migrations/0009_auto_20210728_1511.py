# Generated by Django 3.1.8 on 2021-07-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210728_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaluser',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='historicaluser',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='user',
            name='languages',
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(blank=True, null=True, to='users.Language'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='tags',
        ),
        migrations.AddField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='users.Tag'),
        ),
    ]
