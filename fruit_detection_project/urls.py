from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api import views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),       # Admin panel
    path('', views.home, name='home'),     # Home view
    path('api/', include('api.urls')),     # API endpoints
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Add this line
