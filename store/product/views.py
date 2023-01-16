from django.shortcuts import render
from product.forms import *
from order.models import *
from product.models import *


# Create your views here.
# def img(request):
#     return render(request, "main.html")


def category(request):
    context = Category.objects.all()
    return render(request, template_name='main.html', context={"img": context})


def products_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {
        'products': products,
    }
    return render(request, 'products_list.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            User.obgects.get_orcreate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})
