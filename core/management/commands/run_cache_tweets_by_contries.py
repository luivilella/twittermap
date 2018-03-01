from django.core.management.base import BaseCommand
from core.tools.twitter.get_tweets_by_country import cache_tweets_by_country


class Command(BaseCommand):
    help = 'Script to cache the results of tweets_by_countries'

    def handle(self, *args, **options):
        cache_tweets_by_country()
