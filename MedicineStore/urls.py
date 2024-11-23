from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store import views  # Import views from your app

urlpatterns = [
    # Admin URL route
    path('admin/', admin.site.urls),
    path('medicines/', views.medicine_list, name='medicine_list'),
    
    # Home page route
    path('', views.home, name='home'),  # This will render the home view when accessing the root URL
]

# Add static and media file URLs when in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
