import os
os.environ['DJANGO_SETTINGS_MODULE']='seatAllocatorWeb.settings'
import django
django.setup()
from django.http import HttpResponse,HttpResponseRedirect
from createArrangement.forms import NameForm
from createArrangement.forms2 import NameForm2
from createArrangement.forms3 import NameForm3
from django.shortcuts import render
from django.urls import reverse
from .models import classRooms,deptAndSec,addAndDel

"""def index(request):
    return render(request,"createArrangement/index.html")
def index2(request):
    return render(request,"createArrangement/index2.html")"""
def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index2"))
    else:
        form = NameForm()
        return render(request,'createArrangement/index.html',{'form':form})

def index2(request):
    if request.method == 'POST':
        form2 = NameForm2(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse("index3"))
    else:
        form2 = NameForm2()
        return render(request,'createArrangement/index2.html',{'form2':form2})

def index3(request):
    if request.method == 'POST':
        form3 = NameForm3(request.POST)
        if form3.is_valid():
            form3.save()
            return HttpResponseRedirect(reverse("getresult"))
    else:
        form3 = NameForm3()
        return render(request,'createArrangement/index3.html',{'form3':form3})


def getobjects1():
    data1=classRooms.objects.all()
    obj1=data1.get()
    string1=str(obj1)
    file = open("file1.py", "w")
    file.write(string1)
    print("getfile1 in views")
    return 2
def getobjects2():
    data1=deptAndSec.objects.all()
    obj1=data1.get()
    string1=str(obj1)
    file = open("file2.py", "w")
    file.write(string1)
    print("getfile2 in views")
    return 2
def getobjects3():
    data1=addAndDel.objects.all()
    obj1=data1.get()
    string1=str(obj1)
    file = open("file3.py", "w")
    file.write(string1)
    print("getfile3 in views")
    return 2
def deletion():
    blogs = classRooms.objects.all()
    blogs.delete()
    blogs2 = deptAndSec.objects.all()
    blogs2.delete()
    blogs3 = addAndDel.objects.all()
    blogs3.delete()