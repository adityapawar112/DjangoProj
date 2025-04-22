from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Define the home view
@login_required(login_url='login')  # Use the LOGIN_URL setting from settings.py
def home(request): 
    prod = Product.objects.all()  # Fetch all products from the database
    fm = ProductForm() 
    if request.method == 'POST':
        fm = ProductForm(request.POST, request.FILES)  # Bind the form with POST data and files
        if fm.is_valid():  # Validate the form data
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm()
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm': fm})  # Render the home.html template with the products context