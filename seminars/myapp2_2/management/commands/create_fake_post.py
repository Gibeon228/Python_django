import random

from django.core.management.base import BaseCommand

from myapp2_2.models import Post


class Command(BaseCommand):
    help = "Generate fake authors."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            post = Post(title=f'Title{i}',
                            post=f'Post{i}',
                            publish_date='2000-01-01',
                            author=random.randint(1, 10),
                            categoty=random.randint(1, 10),
                            views=random.randint(1, 1000),
                            publish=random.randint(0, 1))
            post.save()
