from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from products.models import Product

@login_required
def index(request):
    products = Product.objects.filter(seller=request.user)

    return render(request, 'dashboard/index.html', {
        'products': products
    })

