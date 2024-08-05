# Generated by Django 5.0.7 on 2024-08-05 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_car_account_remove_comment_account_car_user_and_more'),
        ('users', '0002_cosmeticrole_color'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountcosmeticroles',
            name='account',
        ),
        migrations.RemoveField(
            model_name='accountcosmeticroles',
            name='cosmetic_role',
        ),
        migrations.CreateModel(
            name='UserCosmeticRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosmetic_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cosmeticrole')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='AccountCosmeticRoles',
        ),
    ]
