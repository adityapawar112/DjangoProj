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

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)  # Fetch the product by ID
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)  # Bind the form with POST data and the product instance
        if form.is_valid():  # Validate the form data
            form.save()  # Save the updated product
            return redirect('home') 
    else:
        form = ProductForm(instance=product)  # Redirect to the home page after saving
    return render(request, 'Electronics/edit_product.html', {'form':form})  # Render the edit_product.html template with the form context

def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)  # Fetch the product by ID
    if request.method == 'POST':
        product.delete()  # Delete the product
        return redirect('home')  # Redirect to the home page after deleting
    return render(request, 'Electronics/delete_product.html', {'product':product})  # Render the delete_product.html template with the product context