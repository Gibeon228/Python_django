import random

from django.core.management.base import BaseCommand

from myapp2_2.models import Category


class Command(BaseCommand):
    help = "Generate fake authors."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            category = Category(name=f'Categoty{i}')
            category.save()
