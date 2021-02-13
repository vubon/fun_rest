FROM python:3.8

ENV PYTHONUNBUFFERED 1
MAINTAINER vubon.roy@gmail.com

# Project Files and Settings
ARG PROJECT=fun_rest
ARG PROJECT_DIR=/var/www/${PROJECT}
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
ADD requirements.txt $PROJECT_DIR
RUN pip install -r requirements.txt
COPY . $PROJECT_DIR


# Server
EXPOSE 8000

