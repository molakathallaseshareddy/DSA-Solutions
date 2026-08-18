from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(req):
    return HttpResponse("<h1 align = 'center'>Welcome To Mavensoft System Private Limited <br> This company is Software Solutions provided</h1>")

def home(req):
    return render(req, 'home.html')

def data_show(req):
    std = {'stdroll':248, 'stdname': "Seshareddy", "stdmarks": [45, 54, 67, 43]}
    return render(req, 'data_show.html', std)

def login(req):
    return render(req, 'login.html')

def fullname(req):
    a = req.POST.get('fname')
    b = req.POST.get('lname')
    c = a +" "+ b
    return render(req, 'fullname.html', {'fln': c})
