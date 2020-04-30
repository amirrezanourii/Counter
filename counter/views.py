from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#import datetime
from .models import Count
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request, id):
    num = Count.objects.get(id=id)
    num.mid_number += 1
    num.save()

    return render(request, 'counter/index.html', {'mid_number': num})
