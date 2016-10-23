FROM python:2.7.12-alpine

ARG os=mac64

WORKDIR /data

RUN wget http://chromedriver.storage.googleapis.com/2.24/chromedriver_$os.zip \
  && unzip chromedriver_$os.zip && pip install selenium flask && apk update \
  && apk add nodejs \
  && npm -g install phantomjs

ENV PATH=$PATH:/data

ADD . /data

EXPOSE 5000
ENTRYPOINT python api.py
