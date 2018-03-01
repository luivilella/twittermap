# twittermap

Project goal:

    1. Displays the latest X tweets from Twitter feed

    2. Displays an interactive map of the tweets where it's possible to associate the tweet with a country or other location.
        - For example:
        Look for the occurrence of a country name in a tweet and place it on a map. Not the location of where the tweet originated.

![image](https://user-images.githubusercontent.com/921729/36857283-e8ad9918-1d56-11e8-97b0-728fbf1622f2.png)

# deploy

- Check your docker version:

        $ docker --version
        Docker version 17.12.0-ce, build c97c6d6

        $ docker-compose --version
        docker-compose version 1.18.0, build 8dd22a9

    To install or upgrade the docker version check:

    - https://docs.docker.com/install/
    - https://docs.docker.com/compose/install/

- Make sure you have all the [Twitter](https://apps.twitter.com) and [Google Maps](https://developers.google.com/maps/documentation/javascript/get-api-key) APIs keys.

- Start the deploy:

        ./scripts/deploy.sh

# Cache
Twitter has a limit of request per period of the time on their api, so we cache the results on our server.

## Refreshing the cache

To refresh the cache results run the command bellow.

    $ docker-compose exec backend python manage.py run_cache_tweets_by_contries

### tip

When you are running the project locally you can run the command `watch -n <sec>` to refresh the cache every X seconds.

    $ watch -n 600 docker-compose exec backend python manage.py run_cache_tweets_by_contries

# Notes

For this first version I'm not setting up a `Nginx` to serve static files and proxy pass to the django app.
