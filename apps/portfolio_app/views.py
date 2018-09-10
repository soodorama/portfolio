from django.shortcuts import render

def index(request):
    return render(request, "portfolio_app/index.html")

def bio(request):
    return render(request, "portfolio_app/bio.html")

def projects(request):
    return render(request, "portfolio_app/projects.html")

def hobbies(request):
    return render(request, "portfolio_app/hobbies.html")

def travel(request):
    return render(request, "portfolio_app/travel.html")