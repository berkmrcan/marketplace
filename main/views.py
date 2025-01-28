from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "main\index.html", {
                      "products":products
                  })

def contact(request):
    return render(request, "main\contact.html")
