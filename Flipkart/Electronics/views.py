from django.shortcuts import render
from .models import Product  # Import the Product model
# Create your views here.

#Define the home view
def home(request): 
    prod = Product.objects.all() # Fetch all products from the database
    return render(request, 'Electronics/home.html', {'prod':prod}) # Render the home.html template with the products context
