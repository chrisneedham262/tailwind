from django.shortcuts import render

def index(request):
    return render(request, 'dashboard.html')

def content(request):
    return render(request, 'content.html')

def team(request):
    return render(request, 'team.html')
 
