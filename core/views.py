from django.shortcuts import render
from django.http  import HttpRequest, HttpResponse
# Create your views here.


def landing(req:HttpRequest) -> HttpResponse:
  
  
  
  return render(req, "landing.html")