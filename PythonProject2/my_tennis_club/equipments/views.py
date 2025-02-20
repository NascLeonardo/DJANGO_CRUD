from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
from .models import Equipment

def equipments(request):
    myequipments = Equipment.objects.all().values()
    template = loader.get_template('all_equipments.html')
    context = {
        'myequipments': myequipments,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    myequipment = Equipment.objects.get(id=id)
    template = loader.get_template('details_equipment.html')
    context =  {
        'myequipment': myequipment
    }
    return HttpResponse(template.render(context,request))