# Generated by Django 5.0.7 on 2024-08-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carimage',
            name='image',
            field=models.ImageField(null=True, upload_to='car_images/'),
        ),
    ]
