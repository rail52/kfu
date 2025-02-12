from django.shortcuts import render

from web.models import WORKER
# Create your views here.

def index(request):
    WORKER.objects.create(name=1234)
    print(WORKER.objects.all())
    return render(request, 'index.html')