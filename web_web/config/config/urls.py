from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main app
    path('', include('photoapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)