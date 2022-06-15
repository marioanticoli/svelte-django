# Simple Django+Svelte kit+Tacit CSS skeleton

## 1. Prerequisites
Please make sure **docker** and **docker-compose** are available on your machine.

## 2. Obtain the source code

`git clone git@github.com:marioanticoli/svelte-django.git`

Alternatively extract the compressed file to any directory and execute the commands from the project root.

## 3. Run

### Development

#### Run FE
`npm run dev --`

#### Run BE
`python manage.py runserver`

### Production

#### Build FE
`cd frontend && npm run build`

#### Migrations
`docker-compose run backend python manage.py migrate`

#### Static Files
`docker-compose run backend python manage.py collectstatic`

#### Services
`docker-compose up`

#### Other commands

##### Stop
`docker-compose stop`

##### Start (after first time)
`docker-compose start`