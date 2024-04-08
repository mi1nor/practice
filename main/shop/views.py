from django.shortcuts import render, redirect, get_object_or_404

# Импортируем декоратор login_required
from django.contrib.auth.decorators import login_required
# Импортируем форму для регистрации
from django.contrib.auth.forms import UserCreationForm
# Импортируем функции для авторизации
from django.contrib.auth import authenticate, login

from .models import Product, Cart, CartItem


def index_page(request):
    context = {
        'page_name': 'TealuxE',
    }

    return render(request, 'shop/index_page.html', context)


def registration_page(request):
    context = {'page_name': "Registration Page"}

    if request.method == 'POST':  # Если пришёл POST-запрос
        # Используем форму Django и сразу помещаем в неё данные
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():  # Если с формой всё в порядке
            reg_form.save()  # Делаем запись в БД (сохраняем пользователя)

            # Получаем имя пользователя с формы
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get(
                'password1')  # Получаем пароль пользователя
            # Получение пользователя
            user = authenticate(username=username, password=password)
            # Войти в пользователя по запросу (для конкретного клиента)
            login(request, user)

            return redirect('/')  # Переходим на домашнюю страницу
    else:  # Если к нам пришёл просто запрос
        reg_form = UserCreationForm()  # Создаём пустую форму

    context['reg_form'] = reg_form  # Добавляем форму в context

    return render(request, 'registration/registration_page.html', context)


@login_required
def profile_page(request):
    return render(request, 'profile/profile_page.html')


@login_required
def edit_profile(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        # UserProfile(user=request.user, first_name=first_name, last_name=last_name, email=email).save()

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('shop:profile-page')

    return render(request, 'profile/edit_profile.html')


@login_required
def view_cart(request):
    user_cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.product.price *
                      item.quantity for item in user_cart_items)
    return render(request, 'cart/view_cart.html', {'cart_items': user_cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user_cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_item, created = CartItem.objects.get_or_create(
        cart=user_cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop:view_products')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('shop:view_cart')


@login_required
def clear_cart(request):
    try:
        user_cart = Cart.objects.get(user=request.user)
        user_cart.cartitem_set.all().delete()
    except Cart.DoesNotExist:
        pass  # Если корзина не существует, просто продолжаем
    return redirect('shop:view_cart')


def view_products(request):
    products = Product.objects.all()
    return render(request, 'cart/products.html', {'products': products})


def single_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # Получаем ссылку, по которой пользователь перешел на текущую страницу
    referrer_url = request.META.get('HTTP_REFERER', None)
    return render(request, 'cart/single_product.html', {'product': product, 'referrer_url': referrer_url})
