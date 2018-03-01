from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tweets-by-countries', views.TweetsByCountriesView.as_view()),
]
