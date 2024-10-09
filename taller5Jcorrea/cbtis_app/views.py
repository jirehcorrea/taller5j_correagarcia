from django.shortcuts import render

# Create your views here.
def verlista(request):
    return render (request,'index.html')
