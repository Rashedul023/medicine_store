from django.shortcuts import render, get_object_or_404
from .models import Medicine,Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    medicines = Medicine.objects.all()  # Retrieve all medicines
    context = {
        'medicines': medicines
    }
    return render(request, 'index.html', context)


def medicine_list(request):
    medicines = Medicine.objects.all()
    paginator = Paginator(medicines, 18)  # 24 medicines per page

    page = request.GET.get('page')
    try:
        medicines = paginator.page(page)
    except PageNotAnInteger:
        medicines = paginator.page(1)
    except EmptyPage:
        medicines = paginator.page(paginator.num_pages)

    return render(request, 'medicine_list.html', {'medicines': medicines})

def medicine_detail(request, medicine_id):
    # Get the medicine by ID or return a 404 if not found
    medicine = get_object_or_404(Medicine, id=medicine_id)
    return render(request, 'medicine_detail.html', {'medicine': medicine})

def search_results(request):
    query = request.GET.get('q')
    results = Medicine.objects.filter(name__icontains=query) if query else []
    
    related_medicines = []
    if results:
        related_diseases = set(
            disease.strip() 
            for medicine in results 
            for disease in medicine.diseases.split(',')
        )
        # Filter by any disease match
        related_medicines = Medicine.objects.filter(
            diseases__iregex=r'\b(' + '|'.join(related_diseases) + r')\b'
        ).exclude(id__in=results)
    
    return render(request, 'search_results.html', {
        'medicines': results,
        'related_medicines': related_medicines,
        'query': query
    })


def category_products(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    medicines_list = Medicine.objects.filter(category=category)
    
    # Pagination logic
    paginator = Paginator(medicines_list, 18) 
    page_number = request.GET.get('page') 
    medicines = paginator.get_page(page_number)

    return render(request, 'category_products.html', {
        'category': category,
        'category_name': category_name,
        'medicines': medicines,
    })