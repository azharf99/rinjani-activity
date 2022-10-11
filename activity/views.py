from django.shortcuts import render, redirect
from activity.models import General, Food, Breast, Sleep, Hygiene, Diaper, Medicine
from django.contrib.auth.models import User
from activity.form import GeneralForm, FoodForm, BreastForm, SleepForm, HygineForm, MedicineForm, DiaperForm

# Create your views here.

def index(request):
    nama = {
        'nama' : User
    }
    return render(request, 'home.html', context=nama)

def general(request):
    datas = General.objects.order_by('-tanggal')
    form = GeneralForm()
    context = {
        'datas': datas,
        'form': form,
    }

    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('general')
    else:
        form = GeneralForm()

    return render(request, 'general.html', context=context)

def general_detail(request, pk):
    detail = General.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'general_detail.html', context=context)

def food(request):
    datas = Food.objects.order_by('-tanggal')
    form = FoodForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        tanggal = request.POST.get('tanggal')
        waktu = request.POST.get('waktu')
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food')
    else:
        form = FoodForm()
    return render(request, 'food.html', context=context)

def food_detail(request, pk):
    detail = Food.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'food_detail.html', context=context)

def breast(request):
    datas = Breast.objects.order_by('-tanggal')
    form = BreastForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = BreastForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('breast')
    else:
        form = BreastForm()

    return render(request, 'breast.html', context=context)

def breast_detail(request, pk):
    detail = Breast.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'breast_detail.html', context=context)

def sleep(request):
    datas = Sleep.objects.order_by('-tanggal')
    form = SleepForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = SleepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sleep')
    else:
        form = SleepForm()
    return render(request, 'sleep.html', context=context)

def sleep_detail(request, pk):
    detail = Sleep.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'sleep_detail.html', context=context)

def hygiene(request):
    datas = Hygiene.objects.order_by('-tanggal')
    form = HygineForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = HygineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hygiene')
    else:
        form = HygineForm()
    return render(request, 'hygiene.html', context=context)

def hygiene_detail(request, pk):
    detail = Hygiene.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'hygiene_detail.html', context=context)

def diaper(request):
    datas = Diaper.objects.order_by('-tanggal')
    form = DiaperForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = DiaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaper')
    else:
        form = DiaperForm()
    return render(request, 'diaper.html', context=context)

def diaper_detail(request, pk):
    detail = Diaper.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'diaper_detail.html', context=context)

def medicine(request):
    datas = Medicine.objects.order_by('-tanggal')
    form = MedicineForm()
    context = {
        'datas': datas,
        'form': form,
    }
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine')
    else:
        form = MedicineForm()
    return render(request, 'medicine.html', context=context)

def medicine_detail(request, pk):
    detail = Medicine.objects.get(id=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'medicine_detail.html', context=context)