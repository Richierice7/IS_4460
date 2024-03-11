# Generated by Django 5.0.1 on 2024-03-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(max_length=11)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
            ],
        ),
    ]
