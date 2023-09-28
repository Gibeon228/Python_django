from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .forms import ProductForm, ImageForm
from django.core.files.storage import FileSystemStorage

from .models import Client, Product, Order


def index(request):
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("This is the about page.")


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    date = datetime.now()
    NEED_THIS_DATE = date - timedelta(days=7)
    orders = Order.objects.filter(client=client).all()
    products = Product.objects.filter(order for order in orders).first()
    return render(request, 'myapp/client_orders.html', {'client': client, 'products': products})


class OrderProductsView(ListView):
    model = Order
    template_name = '/myapp/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Client.objects.get(pk=self.kwargs['pk'])
        orders = Order.objects.filter(customer=customer).all()
        from django.db import connection
        print(connection.queries)
        context['orders'] = orders
        return context


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(name=name, description=description, price=price, quantity=quantity)
            product.save()
            message = 'Продукт добавлен'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp/product_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form': form})
