from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

# def service(request):
#     return render(request,'service.html')
    #return HttpResponse("this is Services page")

def contect(request):
    return render(request,'contect.html')
    #return HttpResponse("this is contect page")

def help(request):
    return render(request,'help.html')
    #return HttpResponse("this is Help page")