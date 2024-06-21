# Generated by Django 5.0.6 on 2024-06-17 14:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_founded', models.DateField(default=django.utils.timezone.now)),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to='cars/media/brandLogo')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='cars/media/carPicture')),
                ('car_price', models.IntegerField()),
                ('car_quantity', models.IntegerField()),
                ('car_description', models.TextField(max_length=400)),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.brand')),
            ],
        ),
    ]