from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}', email=f'mail{i}@mail', phone='88005553535', address='Moscow')
            product = Product(name=f'Product{i}', description=f'Text{i}', price=f'{i}{i + 1}', quantity=f'{i}')
            client.save()
            product.save()