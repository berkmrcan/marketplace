from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:pk>', views.detail, name="detail"),
    path('new/', views.new, name="new")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)