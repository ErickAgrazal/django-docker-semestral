FROM python:3.6.3-stretch
MAINTAINER Erick Agrazal "erick.agrazal@gmail.com"
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD ./src/requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./src/ /code/
ADD ./utilities/ /code/utilities/
