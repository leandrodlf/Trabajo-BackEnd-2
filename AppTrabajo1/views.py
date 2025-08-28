from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'AppTrabajo1/home.html')
def about(request):
    return render(request, 'AppTrabajo1/about.html')