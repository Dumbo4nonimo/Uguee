from django.shortcuts import render

def welcome(request):
    return render(request, 'api/welcome.html')