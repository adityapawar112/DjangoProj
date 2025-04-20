from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from importlib import import_module  # Import for dynamic form loading

def generic_edit_product(request, app_name, model_name, product_id):
    Product = apps.get_model(app_name, model_name)  # Dynamically get the model using model_name
    forms_module = import_module(f'{app_name}.forms')  # Import the forms module of the app
    Form = getattr(forms_module, 'ProductForm')  # Get the ProductForm class from the forms module
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    if request.method == 'POST':
        form = Form(request.POST, request.FILES, instance=product)  # Bind the form with POST data and the product instance
        if form.is_valid():  # Validate the form data
            form.save()  # Save the updated product
            return redirect(f'{app_name}:home')  # Redirect to the home page
    else:
        form = Form(instance=product)
    return render(request, f'{app_name}/edit_product.html', {'form': form})  # Render the edit_product.html template

def generic_delete_product(request, app_name, model_name, product_id):
    Product = apps.get_model(app_name, model_name)  # Dynamically get the model using model_name
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    if request.method == 'POST':
        product.delete()  # Delete the product
        return redirect(f'{app_name}:home')  # Redirect to the home page
    return render(request, f'{app_name}/delete_product.html', {'product': product})  # Render the delete_product.html template
