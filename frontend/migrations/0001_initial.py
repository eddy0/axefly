# Generated by Django 3.1.6 on 2021-02-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('password', models.IntegerField(default='123')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
