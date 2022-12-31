from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht


def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index.html', s)
def dht112(request):
    tab = Dht.objects.all()
    s = {'tab': tab}

    return render(request, 'index2.html', s)
# Create your views here.
def dht113(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index3.html', s)

def dht114(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'index4.html', s)
def dhttabjr1(request):
    tab=Dht.objects.all()[19:34]
    s1={'tab' : tab}
    return render(request,'tabjr1.html',s1)
def dhtgrajr1(request):
    tab = Dht.objects.all()[19:34]
    s2 = {'tab': tab}
    return render(request, 'grajr1.html', s2)
def data48(request):
    tab=Dht.objects.all()[6:13]
    s3={'tab':tab}
    return render(request, 'jr2.html', s3)
def graph48(request):
    tab=Dht.objects.all()[6:13]
    s4={'tab':tab}
    return render(request, 'graph48.html', s4)
def data72(request):
    tab=Dht.objects.all()[6:20]
    s5={'tab':tab}
    return render(request, 'jr3.html', s5)
def graph72(request):
    tab=Dht.objects.all()[6:20]
    s6={'tab':tab}
    return render(request, 'graph72.html', s6)