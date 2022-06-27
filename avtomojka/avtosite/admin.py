from django.contrib import admin
from django.utils.safestring import mark_safe
from .forms import *


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Phone', 'Number', 'Wash', 'Salon', 'Avto', 'HydroShine', 'get_a', 'get_p')
    list_display_links = ('id', 'Phone', 'Number')

    def get_a(self, object):
        a = object.date_update.strftime('%d')
        b = object.date_update.strftime('%m.%Y')
        t = object.Time.time

        if object.Time.day:
            return mark_safe(f"<p>{int(a)+1}.{b} {t}:00</p>")
        else:
            return mark_safe(f"<p>{a}.{b} {t}:00</p>")

    get_a.short_description = "Время записи"


    def get_p(self, object):
        w = object.Wash.price
        s = object.Salon.price
        h = object.HydroShine
        a = object.Avto.kooficent
        sum = (w+s)*a
        sum2 = sum+1000*a
        if h:
            if object.Wash.pk == 1 and object.Salon.pk == 3:
                return mark_safe(f"<p>{sum2*0.85}</p>")
            elif object.Wash.pk == 2 and object.Salon.pk == 2:
                return mark_safe(f"<p>{sum2*0.75}</p>")
            elif object.Wash.pk == 2 and object.Salon.pk == 3:
                return mark_safe(f"<p>{sum2*0.80}</p>")
            else:
                return mark_safe(f"<p>{sum2}</p>")
        else:
            return mark_safe(f"<p>{sum}</p>")

    get_p.short_description = "Цена всех услуг"


class WashAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')



class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')



class AvtoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'kooficent')



class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')



admin.site.register(Wash, WashAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Avto, AvtoAdmin, verbose_name="Автомобиль")
admin.site.register(Applications, ApplicationsAdmin)



