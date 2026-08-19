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

def register(req):
    if req.method == 'POST':
        a = req.POST.get('cid')
        b = req.POST.get('cname')
        c = req.POST.get('bno')
        e1 = Cust(cid = a, cname= b, busno = c)
        e1.save()
        return render(req, 'register.html', {"msg":"Data Inserted"})
    else:
        return render(req,"register.html")