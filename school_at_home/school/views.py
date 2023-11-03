from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import school, ClassName

def index(request):

    context = {}

    return render(request,'index.html', context=context)

class schoolView(generic.ListView):
    model = school


def schoolDetail(requset, id):
    try:
        x = school.objects.get(id = id)
    except school.DoesNotExist:
        raise Http404('School does not exist')
    
    context = {
        'x': x
    }
    
    return render (requset, 'school/school_detail.html', context = context)

def classDetail (request, id):
    try:
        y = ClassName.objects.get(id = id)
    except:
        raise Http404('Class does not exist')
    
    context ={
        'y': y
    }

    return render(request, 'school/class_detail.html', context = context)
