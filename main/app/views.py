from django.shortcuts import render, HttpResponse, redirect
from .models import Hardware
from django.contrib import messages
import csv

# Create your views here.

def user_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')

        hardware = Hardware(
            name=name,
            model=model,
            price=price,
        )
        hardware.save()
        return render(request, 'user_form.html')
        
    return render(request, "user_form.html")

def success(request):
    return render(request, 'success.html')

def start(request):
    return render(request, 'start.html')

def redirect_start(request):
    return redirect('start')


def output_data(request):
    employees = Hardware.objects.all()
    return render(request, 'output_data.html', {'employees': employees})

def download_excel(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="employee_data.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['Name', 'Modell', 'Preis', 'Datum'])

    employees = Hardware.objects.all().values_list('name', 'model', 'price', 'date')
    for employee in employees:
        name, model, price, date = employee

        price = int(price)
        date = date.strftime('%d.%m.%Y')
        writer.writerow([name, model, price, date])

    return response