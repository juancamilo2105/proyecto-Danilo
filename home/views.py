from django.shortcuts import render

def store(request):
     context = {}
     return render(request, 'tienda/store.html', context)

def cart(request):
     context = {}
     return render(request, 'tienda/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'tienda/checkout.html', context)
