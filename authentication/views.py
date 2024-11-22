from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Renders the index.html template from the authentication/templates folder
