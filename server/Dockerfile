# base image
FROM python:3.7-alpine

# install dependencies
RUN apk update
RUN apk add --virtual build-deps gcc python-dev musl-dev
RUN apk add postgresql-dev
RUN apk add netcat-openbsd

# create and set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app
