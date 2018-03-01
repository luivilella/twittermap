from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .tools.twitter.get_tweets_by_country import get_tweets_by_country
from .tools.cache import cache


class IndexView(View):
    def get(self, request):
        return render(request, 'core/index-page.html')


class TweetsByCountriesView(View):

    @cache.cache('TweetsByCountriesView.get_results', expire=120)
    def get_results(self):
        return dict(data=get_tweets_by_country())

    def get(self, request):
        return JsonResponse(self.get_results())
