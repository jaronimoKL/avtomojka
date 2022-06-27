import datetime
from django.shortcuts import render, redirect
from avtosite.forms import Zapis
from .models import *


def index(request):
    posts = Applications.objects.all()
    ttt = posts.count()
    ty = Time.objects.all()

    if request.method == 'POST':
        form = Zapis(request.POST, request.FILES)
        if form.is_valid():
            time_value = form.cleaned_data["Time"]
            time_value.use = True
            time_value.save()
            #print(form.cleaned_data)
            form.save()
            return redirect('/')
    else:
        form = Zapis()

    now = datetime.datetime.now()
    now1 = now.strftime('%d.%m.%Y')
    tomorrow = now + datetime.timedelta(days=1)
    tim = tomorrow.strftime('%d.%m.%Y')
    NH = now.strftime('%H')

    return render(request, "avtosite/index.html", { "zxz": ttt, "now": now, "tim": tim, "NH": int(NH), "now1": now1, 'ttt': posts, 'form': form, 'ty': ty})


