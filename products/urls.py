from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('<int:pk>', views.detail, name="detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('new/', views.new, name="new"),
    path('', views.products, name="products")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)