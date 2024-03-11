from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'crm.html')

def dashboard(request):
    return render(request,'dashboard.html')

def archive(request):
    return render(request,'archive.html')

def contact(request):
    return render(request,'contact.html')

def pricing(request):
    return render(request,'pricing.html')

def signup(request):
    return render(request,'signup.html')