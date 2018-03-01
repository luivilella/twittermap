import asyncio
import concurrent.futures
from urllib.parse import urlencode
from .api import twitter_api
from ..countries_info import COUNTRIES_NAMES, COUNTRIES_LOCATION_MAP
from ..cache import cache as base_cache


cache = base_cache.get_cache('tweets_by_countries', expire=3600)
cache_view = base_cache.get_cache('tweets_by_countries_for_view', expire=3600)


def filter_by_country(country):
    query = dict(q=country, result_type='recent', count=100)
    return twitter_api.GetSearch(raw_query=urlencode(query))


def cache_country(country):
    results = filter_by_country(country)
    cache.set_value(country, [row.__dict__ for row in results])
    cache_view.set_value(country, len(results))


async def async_cache_tweets_by_country():
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        loop = asyncio.get_event_loop()
        futures_in_cache = []
        futures_not_in_cache = []
        for country in COUNTRIES_NAMES:
            future = loop.run_in_executor(
                executor, cache_country, country
            )
            try:
                cache_view.get_value(country)
                futures_in_cache.append(future)
            except KeyError:
                futures_not_in_cache.append(future)

        for _ in await asyncio.gather(*futures_not_in_cache):
            pass

        for _ in await asyncio.gather(*futures_in_cache):
            pass


def cache_tweets_by_country():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_cache_tweets_by_country())


def get_tweets_by_country():
    contries_tweets = []
    for country in COUNTRIES_NAMES:
        try:
            number_of_tweets = cache_view.get_value(country)
        except KeyError:
            continue

        contries_tweets.append(dict(
            country=country,
            number_of_tweets=number_of_tweets,
            location=COUNTRIES_LOCATION_MAP[country]
        ))
    return contries_tweets
