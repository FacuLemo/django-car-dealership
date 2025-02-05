# Generated by Django 5.0.7 on 2024-11-05 16:43

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_car_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brand_images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='car',
            name='bought',
            field=models.BooleanField(default=False, verbose_name='bought'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.carmodel', verbose_name='car_model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.carstatus', verbose_name='car_status'),
        ),
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cars.city', verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(null=True, upload_to='car_images/', verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='seller'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='car'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='carimage',
            name='image',
            field=models.ImageField(null=True, upload_to='car_images/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.brand', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)], verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='carstatus',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.province', verbose_name='province'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='car'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=350, verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='province',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.country', verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userboughtcars',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='car'),
        ),
        migrations.AlterField(
            model_name='userboughtcars',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='userboughtcars',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
