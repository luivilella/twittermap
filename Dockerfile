FROM python:3.6.4

EXPOSE 8000

ADD . /deploy

WORKDIR /deploy

RUN pip install -r requirements.txt

CMD ['python', 'manage.py', 'runserver']
