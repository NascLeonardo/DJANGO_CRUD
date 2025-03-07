from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Member
from .models import Plan

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context =  {
        'mymember': mymember
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def new_member(request):
    myplans = Plan.objects.all().values()
    template = loader.get_template('new_member.html')
    context = {
        'myplans': myplans
    }
    return HttpResponse(template.render(context, request))

    

def create_member(request):
    errors = []
    if 'firstname' not in request.POST or request.POST['firstname'] == '':
        errors.append("Firstname can't be empty!")
    else:
        firstname   = request.POST['firstname']

    if 'lastname' not in request.POST or request.POST['lastname'] == '':
        errors.append("Lastname can't be empty!")
    else:
        lastname   = request.POST['lastname']
    
    if 'phone' not in request.POST or request.POST['phone'] == '':
        errors.append("Phone can't be empty!")
    else:
        phone   = request.POST['phone']
        if Member.objects.filter(phone=phone).exists():
            errors.append("Phone number already exists!")
    if 'plan' not in request.POST or request.POST['plan'] == '':
        errors.append("Plan can't be empty!")
    else:
        plan   = Plan.objects.filter(id=request.POST['plan']).first()
        
    
    # Check if there's any members with the same phone number
    

    if len(errors) > 0:
        context =  {
            'errors': errors
        }
        template = loader.get_template('new_member.html')
        return HttpResponse(template.render(context,request))
    else:
        member = Member(firstname=firstname, lastname=lastname, phone=phone, plan=plan)
        member.save()
        return HttpResponseRedirect(reverse('members'))

def delete(request, id):
    mymember = Member.objects.get(id=id)
    mymember.delete()

    return HttpResponseRedirect(reverse('members'))

def update(request, id):
    myplans = Plan.objects.all().values()
    mymember = Member.objects.get(id=id)
    template = loader.get_template('update.html')
    context =  {
        'mymember': mymember,
        'myplans': myplans
    }
    return HttpResponse(template.render(context,request))

def update_member(request, id):
    mymember = Member.objects.get(id=id)
    mymember.firstname = request.POST['firstname']
    mymember.lastname = request.POST['lastname']
    mymember.phone = request.POST['phone']
    mymember.plan = Plan.objects.filter(id=request.POST['plan']).first()


    mymember.save()
    template = loader.get_template('update.html')

    return HttpResponseRedirect(reverse('members'))