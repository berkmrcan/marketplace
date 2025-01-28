from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Product
from .forms import NewProductForm

# Create your views here.

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {
        'product': product
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            return redirect('/')
    else:
        form = NewProductForm()

    return render(request, 'products/form.html', {
        'form': form,
        'title': 'New Product'
    })