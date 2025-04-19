from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:product_id>', views.edit_product, name='edit_product'),  # Edit product URL
    path('delete/<int:product_id>', views.delete_product, name='delete_product'),  # Delete product URL
]