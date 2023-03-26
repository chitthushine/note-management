#
# 1. start new docker image
#
FROM python:3.9.11

# Install additional packages
RUN apt clean all
RUN apt update
RUN apt install -y gettext build-essential python3-dev python3-pip python3-setuptools

# Location of source code
ENV PROJECT_ROOT /opt/app
RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

# Copying requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy other files.
COPY . .