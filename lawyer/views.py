from django.http import HttpResponse
from django.shortcuts import render
from lawyers.models import lawyers

def home(request):
    advocates = lawyers.objects.all()

    context = {
        'advocates' : advocates,
    }
    return render(request, 'home.html', context)