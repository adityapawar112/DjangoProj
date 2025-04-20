from django.shortcuts import render, redirect
from .models import CloProduct  # Import the CloProduct model
from .forms import ProductForm

# Create your views here.

# Define the home view
def home(request): 
    prod = CloProduct.objects.all()  # Fetch all clothing products from the database
    fm = ProductForm() 
    if request.method == 'POST':
        fm = ProductForm(request.POST, request.FILES)  # Bind the form with POST data and files
        if fm.is_valid():  # Validate the form data
            fm.save()
            return redirect('/clothing/')  # Redirect to the clothing.html page
    else:
        fm = ProductForm()
    return render(request, 'Clothing/clothing.html', {'prod': prod, 'fm': fm})  # Render the clothing.html template with the products context

# Removed edit_product and delete_product as they are now handled by generic views