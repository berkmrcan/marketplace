from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from main.views import index, contact

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('contact', contact, name="contact")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)