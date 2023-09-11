import logging

from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

from .models import Client, Product, Order

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    logger.debug('About page accessed')
    return HttpResponse("This is the about page.")


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    date = datetime.now()
    NEED_THIS_DATE = date - timedelta(days=7)
    orders = Order.objects.filter(client=client, date_ordered__lt=NEED_THIS_DATE).all()
    products = Product.objects.filter(order for order in orders).first()
    return render(request, 'myapp/client_orders.html', {'client': client, 'products': products})

