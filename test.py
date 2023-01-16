
Модели:
- Пользователь (имя, пароль, адрес электронной почты, адрес доставки)
- Продукт (название, описание, цена, картинка, категория)
- Корзина покупок (список продуктов и их количество, общая сумма)

Формы:
- Авторизации/регистрации (имя, пароль, адрес электронной почты)
- Форма добавления продукта (название, описание, цена, картинка, категория)
- Форма добавления продукта в корзину (название, количество)

Шаблоны:
- Шаблон для регистрации/авторизации
- Шаблон для просмотра списка продуктов
- Шаблон для просмотра корзины покупок
- Шаблон для оформления заказа

Функции:
- Функция регистрации/авторизации пользователя
- Функция добавления продукта в корзину
- Функция удаления продукта из корзины
- Функция оформления заказа и перенаправления на страницу оплаты
а теперь напиши код по всем пунктам которые ты описал

Модели:

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    shipping_address = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

Формы:

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.TextField()
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    image = forms.ImageField(upload_to='products')
    category = forms.ModelChoiceField(queryset=Category.objects.all())

class AddProductToCartForm(forms.Form):
    name = forms.CharField(max_length=50)
    quantity = forms.IntegerField()

Шаблоны:

{# registration/login.html #}

<form method="post">
{% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>

{# products/list.html #}

{% for product in products %}
    <div>
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <p>{{ product.price }}</p>
        <img src="{{ product.image.url }}" />
        <p>{{ product.category }}</p>
    </div>
{% endfor %}

{# cart/list.html #}

<h3>Shopping Cart</h3>

{% for product in cart.products %}
    <div>
        <h3>{{ product.name }}</h3>
        <p>{{ product.quantity }}</p>
    </div>
{% endfor %}

<h3>Total Price: {{ cart.total_price }}</h3>

{# checkout/confirm.html #}

<h3>Order Confirmation</h3>

<p>Your order has been placed. Thank you for shopping with us!</p>

Функции:

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('products:list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})

def add_to_cart(request):
    if request.method == 'POST':
        form = AddProductToCartForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['name']
            product = Product.objects.get(name=product_name)
            quantity = form.cleaned_data['quantity']
            shopping_cart, created = ShoppingCart.objects.get_or_create(
                user=request.user,
            )
            shopping_cart.products.add(product, through_defaults={'quantity': quantity})
            shopping_cart.save()
            return redirect('cart:list')
    else:
        form = AddProductToCartForm()

    return render(request, 'cart/list.html', {'form': form})

def list_cart(request):
    shopping_cart = ShoppingCart.objects.get(user=request.user)
    return render(request, 'cart/list.html', {'shopping_cart': shopping_cart})

def confirm_order(request):
    return render(request, 'checkout/confirm.html')