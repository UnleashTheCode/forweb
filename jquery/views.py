from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def jv(request):
    return render(request,'html/javas.html',content_type='text/javascript')