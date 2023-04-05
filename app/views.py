from django.shortcuts import render

from app.models import *

# Create your views here.


def C_Name(request):

    LOC=College.objects.all()
    d={'Colleges':LOC}
    return render(request,'student1.html',context=d)    

    


def S_Name(request):
    LOS=Subjects.objects.all()
    d={'Sub':LOS}

    return render(request,'student2.html',context=d)


def Stu_Name(request):
    LOST=Student.objects.all()
    d={'Stu':LOST}

    return render(request,'student3.html',context=d)
