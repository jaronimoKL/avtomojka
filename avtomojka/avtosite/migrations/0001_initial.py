# Generated by Django 4.0.2 on 2022-06-12 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Автомобиль')),
                ('kooficent', models.FloatField()),
            ],
            options={
                'verbose_name': 'Авто',
                'verbose_name_plural': 'Авто',
            },
        ),
        migrations.CreateModel(
            name='HydroShine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hydroshine', models.BooleanField(verbose_name='Hydro Shine')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Время',
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Услуги для салона')),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Салон',
                'verbose_name_plural': 'Салон',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=13, verbose_name='Время')),
            ],
            options={
                'verbose_name': 'Время',
                'verbose_name_plural': 'Время',
            },
        ),
        migrations.CreateModel(
            name='Wash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Услуги мойки кузова')),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Мойка',
                'verbose_name_plural': 'Мойка',
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(max_length=12, verbose_name='Телефон')),
                ('Number', models.CharField(max_length=20, verbose_name='Номер автомобиля')),
                ('HydroShine', models.BooleanField(verbose_name='Hydro Shine')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('Avto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avtosite.avto', verbose_name='Автомобиль')),
                ('Salon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avtosite.salon', verbose_name='Услуги для салона')),
                ('Time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avtosite.time', verbose_name='Время')),
                ('Wash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avtosite.wash', verbose_name='Услуги мойки кузова')),
            ],
            options={
                'verbose_name': 'Заявки',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-time_create'],
            },
        ),
    ]