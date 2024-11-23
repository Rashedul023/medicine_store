from django.shortcuts import render
from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()  # Retrieve all medicines
    context = {
        'medicines': medicines
    }
    return render(request, 'index.html', context)


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})