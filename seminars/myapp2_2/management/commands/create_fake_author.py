from django.core.management.base import BaseCommand

from myapp2_2.models import Author


class Command(BaseCommand):
    help = "Generate fake authors."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}',
                            lastname= f'Lastname{i}',
                            email=f'mail{i}@mail',
                            bio=f'bio{i} fldbndbnfkdnb',
                            bd='2000-01-01')
            author.save()
