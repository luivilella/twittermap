from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .tools.twitter.get_tweets_by_country import get_tweets_by_country


class IndexView(View):
    def get(self, request):
        return render(request, 'core/index-page.html')


class TweetsByCountriesView(View):

    def get(self, request):
        return JsonResponse(dict(data=get_tweets_by_country()))
