import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("Hello, world!")


def about(request):
    logger.debug('About page accessed')
    return HttpResponse("This is the about page.")
