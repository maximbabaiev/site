from django.shortcuts import render
from product.forms import *
from order_u.models import *
from product.models import *


# Create your views here.
# def img(request):
#     return render(request, "main.html")


def category(request):
    context = Category.objects.all()
    context_product = Product.objects.all()
    return render(request, template_name='main.html', context={"categories": context, "prod": context_product})





def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        User.objects.get_or_create(
            email=form.cleaned_data['user_email'],
            password=form.cleaned_data['password']
        )

    return render(request, 'account.html', {'form': form})
