# Generated by Django 4.1 on 2022-09-01 01:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
