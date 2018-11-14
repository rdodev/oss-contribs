FROM python:3.7-slim

RUN apt-get update

RUN apt-get install -y curl

RUN curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python

ADD . /oss
WORKDIR /oss

RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python", "gh-repo-oss-contrib-xls.py"]