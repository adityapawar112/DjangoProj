from django.urls import path
from utils.generic_views import generic_edit_product, generic_delete_product
from . import views

app_name = 'Electronics'

urlpatterns = [
    path('', views.home, name='home'),  # Register the home view
    path('edit/<int:product_id>/', generic_edit_product, {'app_name': app_name, 'model_name': 'Product'}, name='edit_product'),  # Edit product URL
    path('delete/<int:product_id>/', generic_delete_product, {'app_name': app_name, 'model_name': 'Product'}, name='delete_product'),  # Delete product URL
]