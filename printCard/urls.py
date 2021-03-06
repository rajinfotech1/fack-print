from django.contrib import admin
from django.urls import path, include
from . import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("printAdhar.urls")),
    path('u/', include("userApp.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
