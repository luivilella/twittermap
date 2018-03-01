import asyncio
import concurrent.futures
from urllib.parse import urlencode
from .api import twitter_api
from ..contries_info import COUNTRIES_NAMES
from ..cache import cache as base_cache


cache = base_cache.get_cache('tweets_by_countries', expire=3600)


def filter_by_country(country):
    query = dict(q=country, result_type='recent', count=100)
    return twitter_api.GetSearch(raw_query=urlencode(query))


def cache_country(country):
    cache.set_value(country, filter_by_country(country))


async def async_cache_tweets_by_country():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop = asyncio.get_event_loop()
        futures = []
        for country in COUNTRIES_NAMES[:1]:
            futures.append(loop.run_in_executor(
                executor, cache_country, country
            ))

        for _ in await asyncio.gather(*futures):
            pass


def cache_tweets_by_country():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_cache_tweets_by_country())


def get_tweets_by_country():
    contries_tweets = []
    for country in COUNTRIES_NAMES:
        try:
            contries_tweets.append((country, cache.get_value(country)))
        except KeyError:
            pass
    return contries_tweets
