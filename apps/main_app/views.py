from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Travel
from django.contrib import messages


# Create your views here.
def dashboard(request):
    if "email" not in request.session:
        return redirect('/')

    context = {
        'users': User.objects.all(),
        'cur_user': User.objects.get(id = request.session['id']),
        'trips': Travel.objects.all(),
    }
    return render(request, 'main_app/dashboard.html', context)

def addTrip(request):
    if "email" not in request.session:
        return redirect('/')
    context = {
        'tripOrginizer': User.objects.get(id = request.session['id'])
    }
    return render(request, 'main_app/add.html', context)

def createTrip(request):
    if "email" not in request.session:
        return redirect('/')
    # results = Travel.objects.validator(request.POST)
    # if results['status'] == True:
    Travel.objects.create(destination = request.POST['destination'], desc = request.POST['desc'], dateFrom= request.POST['dateFrom'], dateTo = request.POST['dateTo'], tripOrginizer = request.POST['tripOrginizer'])
    return redirect('/main/dashboard')

def show(request, id):
    context = {
        'cur_trip': Travel.objects.get(id = id),
        'users': User.objects.exclude(id = request.session['id']),
        'cur_user': User.objects.get(id = request.session['id']),
        'trips': Travel.objects.all()
    }
    return render (request, 'main_app/show.html', context)

def link(request, id):
    logged_user = User.objects.get(id = request.session['id'])
    curTrip = Travel.objects.get(id = id)
    logged_user.travel.add(curTrip)
    return redirect('/main/dashboard')