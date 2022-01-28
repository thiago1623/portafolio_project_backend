# Generated by Django 3.1.8 on 2021-05-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scoreboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('habit', models.ManyToManyField(to='habits.Habit')),
            ],
            options={
                'verbose_name': 'Scoreboard',
                'verbose_name_plural': 'Scoreboards',
            },
        ),
    ]
