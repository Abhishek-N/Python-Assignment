# Generated by Django 2.2.13 on 2021-04-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=56)),
                ('last_name', models.CharField(max_length=56)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]