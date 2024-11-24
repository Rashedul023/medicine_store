from django.shortcuts import render, get_object_or_404
from .models import Medicine,Category

def home(request):
    medicines = Medicine.objects.all()  # Retrieve all medicines
    context = {
        'medicines': medicines
    }
    return render(request, 'index.html', context)


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def medicine_detail(request, medicine_id):
    # Get the medicine by ID or return a 404 if not found
    medicine = get_object_or_404(Medicine, id=medicine_id)
    return render(request, 'medicine_detail.html', {'medicine': medicine})

def search_results(request):
    query = request.GET.get('q')  # Get the search query from the GET request
    results = Medicine.objects.filter(name__icontains=query) if query else []  # Search for medicines by name
    return render(request, 'search_results.html', {'medicines': results, 'query': query})

def category_products(request, category_name):
    # Fetch the category by name
    category = get_object_or_404(Category, name=category_name)

    # Fetch medicines in the category
    medicines = Medicine.objects.filter(category=category)

    return render(request, 'category_products.html', {
        'category': category,
        'medicines': medicines,
    })