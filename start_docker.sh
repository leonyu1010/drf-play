#! /bin/sh

export DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 # enable buildkit
sudo docker compose build
sudo docker compose run --rm web python manage.py migrate
sudo docker compose up
