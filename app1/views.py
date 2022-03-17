from django.shortcuts import render
from app1.models import Bangalore_jobs,Bihar_jobs,Hydrabad_jobs

# Create your views here.

def app1_view(request):
    return render(request,'index.html')

def Bang1(request):
    job_list = Bangalore_jobs.objects.all()
    dic = {'job_list':job_list}
    return render(request,'display.html',context=dic)

def Bihar1(request):
    job_list = Bihar_jobs.objects.all()
    dic = {'job_list':job_list}
    return render(request,'disp2.html',context=dic)

def Hydra1(request):
    job_list = Hydrabad_jobs.objects.all()
    dic = {'job_list':job_list}
    return render(request,'disp3.html',context=dic)
