from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q

from .models import Product
from .forms import NewProductForm, EditProductForm

# Create your views here.

def products(request):
    query = request.GET.get('query','')
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query)|Q(description__icontains=query))

    return render(request, 'products/products.html', {
        'products':products,
        'query':query
    })


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {
        'product': product
    })

@login_required
def new(request):
    if request.method == "POST":
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('products:detail', pk=product.id)
    else:
        form = NewProductForm()

    return render(request, 'products/form.html', {
        'form': form,
        'title': 'New Product'
    })

@login_required
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == "POST":
        form = EditProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:detail', pk=product.id)
    else:
        form = EditProductForm(instance=product)

    return render(request, 'products/form.html', {
        'form': form,
        'title': 'New Product'
    })

@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    product.delete()

    return redirect('dashboard:index')