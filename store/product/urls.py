from django.urls import path
from product.views import *

urlpatterns = [
    # path('', img),
    path('', category),
    path('categories/<int:category_id>/', products_list, name='products_list')
]
