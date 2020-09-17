from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE

def button(request):
    return render(request,'home.html')

def external(request):
    if request.method=="POST":
         inp=request.body('data')
         out=run([sys.executable,'//Users//rudra//JP_NOTEBOOKS//example.py',inp],shell=False,stdout=PIPE)
         return render(request,'home.html')