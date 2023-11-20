from django.shortcuts import render

# Create your views here.
def loop(request):
    d={ 'name':'akshay'}
    return render(request,'index.html',d)
