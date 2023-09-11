from random import choices

from django.core.management.base import BaseCommand
from my_app3.models import Author, Article

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. " \
        "At cupiditate dolorem in, nam possimus similique. " \
        "Ad adipisci aliquid amet aperiam architecto autem " \
        "consequuntur dolore enim et eveniet exercitationem " \
        "hic natus neque optio pariatur placeat praesentium " \
        "qui quisquam quod rem sint velit, veritatis! " \
        "A doloremque enim nostrum rem sunt! " \
        "Adipisci aliquid architecto atque blanditiis explicabo hic quae soluta. " \
        "Amet cumque delectus doloremque earum exercitationem illo iure, rerum."


class Command(BaseCommand):
    help = "Generate fake author and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')


    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                article = Article(
                    title=f'Title-{j}',
                    content="Text from ".join(choices(text, k=64)),
                    author=author
                )
                article.save()
