from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    ProductTag, Product, ProductComment,
    Cart,
)
from blog.models import Post
from django.db.models import Count


def home_view(request):
    products = Product.objects.filter(is_published=True).order_by('-created_at')
    advertised_products = Product.objects.filter(is_advertised=True, is_published=True).order_by('-created_at')[:3]
    latest_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    testimonials = ProductComment.objects.filter(is_active=True).order_by('-created_at')[:3]

    context = {
        'products': products,
        'advertised_products': advertised_products,
        'latest_posts': latest_posts,
        'testimonials': testimonials,
    }

    return render(request, 'index.html', context)


def product_single_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        ProductComment.objects.create(product_id=pk, message=data['comment'],
                                      name=data['name']).save()

        return redirect(f'/product/{pk}')

    product = get_object_or_404(Product, pk=pk)
    comments = ProductComment.objects.filter(product_id=pk).order_by('-created_at')

    context = {
        'product': product,
        'comments': comments,
    }

    return render(request, 'pro-details.html', context)


def category_view(request):
    data = request.GET.get('cat')
    products = Product.objects.filter(category=data).order_by('-created_at')

    context = {
        'products': products,
    }

    return render(request, 'categories.html', context)


def cart_view(request):
    carts = Cart.objects.filter()

    amount = sum([i.quantity * i.product.price_with_discount for i in carts])
    total_amount = amount + 20  # 20 is shipping price

    context = {
        'products': carts,
        'amount': amount,
        'total_amount': total_amount,
    }

    return render(request, 'cart.html', context)


def cart_add_view(request):
    product_id = request.GET.get('product_id')

    product = Product.objects.filter(id=product_id).first()
    Cart.objects.create(product=product).save()

    return redirect('/cart')


def cart_delete_view(request):
    product_id = request.GET.get('product_id')

    product = Product.objects.filter(id=product_id).first()
    Cart.objects.filter(product=product).delete()

    return redirect('/cart')


def checkout_view(request):
    return render(request, 'checkout.html')
