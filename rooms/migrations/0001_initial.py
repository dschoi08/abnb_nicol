# Generated by Django 3.0.12 on 2021-02-02 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140)),
                ('address', models.CharField(max_length=140)),
                ('price', models.IntegerField(help_text='USD per night')),
                ('beds', models.IntegerField(default=1)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
                ('bedrooms', models.IntegerField(default=1)),
                ('bathrooms', models.IntegerField(default=1)),
                ('check_in', models.TimeField(default='00:00:00')),
                ('check_out', models.TimeField(default='00:00:00')),
                ('instant_book', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('file', models.ImageField(upload_to='')),
                ('caption', models.CharField(max_length=140)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
