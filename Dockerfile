FROM python:3.6-alpine
MAINTAINER WaniKanji

ENV PYTHONUNBUFFERED 1

# install numpy
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk add --no-cache --allow-untrusted --repository http://dl-3.alpinelinux.org/alpine/edge/testing hdf5 hdf5-dev
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip install numpy==1.17.4

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /core-api
# collect static files
RUN python manage.py collectstatic --noinput
WORKDIR /core-api
COPY ./core-api /core-api

RUN adduser -D user
USER user
