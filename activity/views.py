from django.shortcuts import render
from activity.models import General, Food, Breast, Sleep, Hygiene, Diaper, Medicine
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    nama = {
        'nama' : User
    }
    return render(request, 'home.html', context=nama)

def general(request):
    generals_data = General.objects.order_by('-tanggal')
    context = {
        'generals_data': generals_data,
    }
    return render(request, 'general.html', context=context)

def general_detail(request, pk):
    general_data = General.objects.get(id=pk)
    context = {
        'general_data': general_data,
    }
    return render(request, 'general_detail.html', context=context)

def food(request):
    foods_data = Food.objects.order_by('-tanggal')
    context = {
        'foods_data': foods_data,
    }
    return render(request, 'food.html', context=context)

def food_detail(request, pk):
    food_data = Food.objects.get(id=pk)
    context = {
        'food_data': food_data,
    }
    return render(request, 'food_detail.html', context=context)

def breast(request):
    breasts_data = Breast.objects.order_by('-tanggal')
    context = {
        'breasts_data': breasts_data,
    }
    return render(request, 'breast.html', context=context)

def breast_detail(request, pk):
    breast_data = Breast.objects.get(id=pk)
    context = {
        'breast_data': breast_data,
    }
    return render(request, 'breast_detail.html', context=context)

def sleep(request):
    sleeps_data = Sleep.objects.order_by('-tanggal')
    context = {
        'sleeps_data': sleeps_data,
    }
    return render(request, 'sleep.html', context=context)

def sleep_detail(request, pk):
    sleep_data = Sleep.objects.get(id=pk)
    context = {
        'sleep_data': sleep_data,
    }
    return render(request, 'sleep_detail.html', context=context)

def hygiene(request):
    hygienes_data = Hygiene.objects.order_by('-tanggal')
    context = {
        'hygienes_data': hygienes_data,
    }
    return render(request, 'hygiene.html', context=context)

def hygiene_detail(request, pk):
    hygiene_data = Hygiene.objects.get(id=pk)
    context = {
        'hygiene_data': hygiene_data,
    }
    return render(request, 'hygiene_detail.html', context=context)

def diaper(request):
    diapers_data = Diaper.objects.order_by('-tanggal')
    context = {
        'diapers_data': diapers_data,
    }
    return render(request, 'diaper.html', context=context)

def diaper_detail(request, pk):
    diaper_data = Diaper.objects.get(id=pk)
    context = {
        'diaper_data': diaper_data,
    }
    return render(request, 'diaper_detail.html', context=context)

def medicine(request):
    medicines_data = Medicine.objects.order_by('-tanggal')
    context = {
        'medicines_data': medicines_data,
    }
    return render(request, 'medicine.html', context=context)

def medicine_detail(request, pk):
    medicine_data = Medicine.objects.get(id=pk)
    context = {
        'medicine_data': medicine_data,
    }
    return render(request, 'medicine_detail.html', context=context)