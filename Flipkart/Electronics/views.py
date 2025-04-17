from django.shortcuts import render, redirect
from .models import Product  # Import the Product model
from .forms import ProductForm

# Create your views here.

#Define the home view
def home(request): 
    prod = Product.objects.all() # Fetch all products from the database
    fm = ProductForm() 
    if request.method == 'POST':
        fm = ProductForm(request.POST)
        if fm.is_valid(): # Validate the form data
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm()
    return render(request, 'Electronics/home.html', {'prod':prod, 'fm':fm}) # Render the home.html template with the products context

