from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.
def home(request):
    return render(request,"cricketplayersdata/home.html")
@login_required(login_url='/accounts/login/')
def players(request):
    return render(request,"cricketplayersdata/players.html")
@login_required(login_url='/accounts/login/')
def coach(request):
    return render(request,"cricketplayersdata/coach.html")

      
