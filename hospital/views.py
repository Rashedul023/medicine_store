from django.shortcuts import render
from django.db.models import Q
from .models import Hospital

def hospital_number(request):
    query = request.GET.get('q', '')  # Get search query from request
    if query:
        hospitals = Hospital.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query)  # Search by name OR address
        )
    else:
        hospitals = Hospital.objects.all()  # Show all hospitals by default

    return render(request, 'hospital.html', {'hospitals': hospitals})
