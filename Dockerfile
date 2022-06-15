# base image
FROM python:3.9-alpine3.15

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#copy the requirements list
COPY ./requirements.txt /tmp

#Create directory to mount volume with source code
#add deps in Alpine
#let pip install required packages
RUN mkdir /backend \
    && apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev libffi-dev \
    && pip install --upgrade pip && pip install -r /tmp/requirements.txt

WORKDIR /backend