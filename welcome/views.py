from imp import load_source
from multiprocessing import context
from re import template
from urllib import request
from django.shortcuts import render
from django.template import loader, RequestContext
from .models import Cars
from django.urls import reverse
from .models import SellInsert
from django.contrib import messages
from .models import cont

from .models import buy
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    template = loader.get_template('Index.html')
    return HttpResponse(template.render())


def sell(request):
    if request.method == "POST":
        if request.POST.get('FirstName') and request.POST.get('LastName') and request.POST.get(
                'ModelName') and request.POST.get('Email') and request.POST.get('PhoneNumber') and request.POST.get(
            'Location') and request.POST.get('Year'):
            saverecord = SellInsert()
            saverecord.FirstName = request.POST.get('FirstName')
            saverecord.LastName = request.POST.get('LastName')
            saverecord.ModelName = request.POST.get('ModelName')
            saverecord.Email = request.POST.get('Email')
            saverecord.PhoneNumber = request.POST.get('PhoneNumber')
            saverecord.Location = request.POST.get('Location')
            saverecord.Year = request.POST.get('Year')
            saverecord.save()
            messages.success(request, "Saved Record Successfully....!")
            return render(request, 'form_sell.html')
    else:

        return render(request, 'form_sell.html')


def fill(request):
    if request.method == "POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get(
                'email') and request.POST.get('phonenumber') and request.POST.get('location') and request.POST.get(
            'year') and request.POST.get('modelname'):
            data = buy()
            data.firstname = request.POST.get('firstname')
            data.lastname = request.POST.get('lastname')
            data.email = request.POST.get('email')
            data.phonenumber = request.POST.get('phonenumber')
            data.location = request.POST.get('location')
            data.year = request.POST.get('year')
            data.modelname = request.POST.get('modelname')
            data.save()
            messages.success(request, "Saved Record Successfully we will contact you soon...!")
            return render(request, "taking.html")
    else:
        return render(request, "taking.html")


def car(request):
    mygarage = Cars.objects.all().values()
    template = loader.get_template("Sell_form.html")
    context = {
        'garage': mygarage
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add1.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['CarName']
    y = request.POST['CarModelYear']
    z = request.POST['Price']
    mycar = Cars(CarName=x, CarModelYear=y, Price=z)
    mycar.save()
    return HttpResponseRedirect(reverse('car'))


def delete(request, id):
    mycar = Cars.objects.get(id=id)
    mycar.delete()
    return HttpResponseRedirect(reverse('car'))


def update(request, id):
    mycar = Cars.objects.get(id=id)
    template = loader.get_template("update1.html")
    context = {
        'mycar': mycar
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    CarName = request.POST['CarName']
    CarModelYear = request.POST['CarModelYear']
    Price = request.POST['Price']
    mycar = Cars.objects.get(id=id)
    mycar.CarName = CarName
    mycar.CarModelYear = CarModelYear
    mycar.Price = Price
    mycar.save()
    return HttpResponseRedirect(reverse('car'))


def contact(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('date'):
            dt = cont()
            dt.name = request.POST.get('name')
            dt.phone = request.POST.get('phone')
            dt.email = request.POST.get('email')
            dt.subject = request.POST.get('subject')
            dt.date = request.POST.get('date')

            dt.save()
            messages.success(request,"Record Safed Successfully we will contact you soon...!")
            return render(request,"contact.html")

    else:
        return render(request,"contact.html")



