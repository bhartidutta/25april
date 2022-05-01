from django.shortcuts import render
from .forms import Customer
# Create your views here.
def djangoform(request):
    fm=Customer()
    return render(request,"display.html",{'form':fm})