FROM python:2.7
LABEL maintainer "Yashit Maheshwary <yashitmaheshwary@gmail.com>"
RUN apt-get update -qq && apt-get install build-essential g++ flex bison gperf ruby perl \ 
  libsqlite3-dev libmariadb-dev-compat libmariadb-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
  postgresql-client \
  libpng-dev libjpeg-dev python libx11-dev libxext-dev -y
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN pip install Django==1.11.29
WORKDIR /code
ADD . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]