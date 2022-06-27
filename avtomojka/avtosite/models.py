from django.db import models
from django.core.validators import RegexValidator


class Wash(models.Model):
    title = models.CharField(max_length=255, verbose_name="Услуги мойки кузова")
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Мойка'
        verbose_name_plural = 'Мойка'

    def __str__(self):
        return self.title

class Salon(models.Model):
    title = models.CharField(max_length=255, verbose_name="Услуги для салона")
    price = models.FloatField(verbose_name="Цена")

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салон'

    def __str__(self):
        return self.title

class Avto(models.Model):
    title = models.CharField(max_length=255, verbose_name="Автомобиль")
    kooficent = models.FloatField(verbose_name="Коофицент", max_length=3)

    class Meta:
        verbose_name = 'Авто'
        verbose_name_plural = 'Авто'

    def __str__(self):
        return self.title

class Time(models.Model):
    title = models.CharField(max_length=13, verbose_name="День и время записи")
    day = models.BooleanField(default=False, verbose_name="Завтрашний день")
    time = models.IntegerField(default=0, max_length=5, verbose_name="Время")
    use = models.BooleanField(default=False, verbose_name="used", blank=True)

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'

    def __str__(self):
        return self.title


class Applications(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Введите телефон в формате: \"+79009009090\"")
    Phone = models.CharField(validators=[phone_regex], max_length=12, verbose_name="Телефон")
    Number = models.CharField(max_length=20, verbose_name="Номер автомобиля")
    Wash = models.ForeignKey('Wash', default=1, on_delete=models.PROTECT, verbose_name="Услуги мойки кузова")
    Salon = models.ForeignKey('Salon', default=1, on_delete=models.PROTECT, verbose_name="Услуги для салона")
    Avto = models.ForeignKey('Avto', default=1, on_delete=models.PROTECT, verbose_name="Автомобиль")
    Time = models.ForeignKey('Time', default=1, on_delete=models.PROTECT, verbose_name="Время", blank=True, unique=True)
    HydroShine = models.BooleanField(verbose_name="Hydro Shine")
    Done = models.BooleanField(verbose_name="Заявка исполнена", default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    date_update = models.DateField(auto_now=True, blank=True)


    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-time_create']
