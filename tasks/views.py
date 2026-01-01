from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("<h1 style='color:green'>This is contact page</h1>")

def show_task(request):
    return HttpResponse("This is show task page")

def show_specific_task(request,id):
    print("id",id)
    print("id type",type(id))
    print("hello")
    print("how are you")
    return HttpResponse("This is specific task page")
def dashboard(request,id):
    return HttpResponse("This is Dashboard")
def admin(request):
    return HttpResponse("This is admin feature implementation")