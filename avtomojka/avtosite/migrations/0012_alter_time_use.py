# Generated by Django 4.0.2 on 2022-06-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avtosite', '0011_time_use_alter_applications_avto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='use',
            field=models.BooleanField(blank=True, default=False, verbose_name='used'),
        ),
    ]
