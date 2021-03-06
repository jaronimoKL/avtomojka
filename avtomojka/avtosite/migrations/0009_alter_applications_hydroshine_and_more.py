# Generated by Django 4.0.2 on 2022-06-13 11:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avtosite', '0008_alter_time_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='HydroShine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avtosite.hydroshine', verbose_name='Hydro Shine'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='Phone',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message='Введите телефон в формате: "+79009009090"', regex='^\\+?1?\\d{9,15}$')], verbose_name='Телефон'),
        ),
    ]
