# MedicineStore/urls.py (Project-Level)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views as auth_views  # Correct import for authentication views
from store import views as store_views  # Import views from the store app

urlpatterns = [
    # Admin URL route
    path('admin/', admin.site.urls),
    
    # Authentication URLs
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout'),
    
    # Home page route
    path('', store_views.home, name='home'),  # This will render the home view when accessing the root URL
    
    # Medicines page route
    path('medicines/', store_views.medicine_list, name='medicine_list'),
    path('medicines/<int:medicine_id>/',store_views.medicine_detail, name='medicine_detail'),
    path('search/', store_views.search_results, name='search_results'),
    path('category/<str:category_name>/', store_views.category_products, name='category_products'),
]

# Add static and media file URLs when in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
