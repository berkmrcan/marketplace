from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('new/<int:product_pk>/', views.new_conversation, name='new'),
    path('<int:pk>/', views.detail, name="detail"),
    path('', views.inbox, name="inbox")
]