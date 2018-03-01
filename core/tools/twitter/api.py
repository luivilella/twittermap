import twitter
from django.conf import settings


twitter_api = twitter.Api(
    consumer_key=settings.TWITTER_CONSUMER_KEY,
    consumer_secret=settings.TWITTER_CONSUMER_SECRET,
    access_token_key=settings.TWITTER_TOKEN_KEY,
    access_token_secret=settings.TWITTER_TOKEN_SECRET,
)
