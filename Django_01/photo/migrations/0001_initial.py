# Generated by Django 4.2.1 on 2023-05-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]