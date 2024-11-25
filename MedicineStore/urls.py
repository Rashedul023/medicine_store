# MedicineStore/urls.py (Project-Level)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views as auth_views  # Correct import for authentication views
from store import views as store_views  # Import views from the store app
from cart import views as cart_views
from hospital import views as hospital_views

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

    # path('cart/', cart_views.view_cart, name='view_cart'),
    # path('cart/add/<int:medicine_id>/', cart_views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/<int:item_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('cart/add/<int:medicine_id>/', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/add/<int:medicine_id>/<int:quantity>/', cart_views.add_to_cart, name='add_to_cart_quantity'),
    path('cart/minus/<int:medicine_id>/<int:quantity>/', cart_views.minus_to_cart, name='minus_to_cart_quantity'),
    path('cart/', cart_views.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', cart_views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', cart_views.checkout, name='checkout'),
    path('health-tips/', auth_views.health_tips, name='health_tips'),

    path('hospitals/', hospital_views.hospital_number, name='hospital_number'),

]

# Add static and media file URLs when in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
