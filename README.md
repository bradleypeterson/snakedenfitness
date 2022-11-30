# Snake Den Fitness
A workout and meal tracking web app

### Getting Started

Setup project environment with virtualenv and pip:

```
$ virtualenv venv
$ source venv/bin/activate
$ cd snakedenfitness/
$ pip install -r requirements.txt
$ python -m pip install channels_redis
$ python -m pip install -U channels["daphne"]

Install Docker:
https://www.docker.com/products/docker-desktop/

$ docker run -p 6379:6379 -d redis:5
$ python manage.py makemigrations community
$ python manage.py sqlmigrate community (migration number ex: 0001)
$ python manage.py migrate
$ python manage.py runserver
```

For deployment:
```
python -m pip install channels_redis
python -m pip install -U channels["daphne"]

Install Docker:
https://www.docker.com/products/docker-desktop/

Then run:
docker run -p 6379:6379 -d redis:5
python manage.py makemigrations community
python manage.py sqlmigrate community 0001
python manage.py migrate
```
