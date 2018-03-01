#!/bin/bash

echo 'Creating the .env file'
cp .env.template .env

echo 'File .env created, check your keys:'
cat .env
read -p "Set all your keys and type [y] to continue [y/n] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
fi

docker-compose build
docker-compose up -d

docker-compose exec backend python manage.py run_cache_tweets_by_contries
