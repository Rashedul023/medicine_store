from django.shortcuts import render
from .models import Medicine  # This should work now after defining the Medicine model

def home(request):
    medicines = Medicine.objects.all()  # Retrieve all medicines
    context = {
        'medicines': medicines
    }
    return render(request, 'index.html', context)
