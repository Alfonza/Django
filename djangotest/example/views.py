from django.shortcuts import render
#from 
# Create your views here.
def home(request):
    my_context={
        "title":"hello everyone....."
    }
    return render(request,"home.html",my_context)
    #render(request,'home.html')