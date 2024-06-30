from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
 return render(request,"staticapp/results.html")
def eat_view(request):
 return render(request,'staticapp/eat.html')
def grocery_view(request):
 return render(request,'staticapp/grocery.html')
def login_view(request):
 return render(request,'staticapp/login.html')
def againlogin_view(request):
 return render(request,'staticapp/results.html')