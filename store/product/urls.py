from django.urls import path
from product.views import *

urlpatterns = [
    # path('', img),
    path('', category),
    path('account/', login)
]
