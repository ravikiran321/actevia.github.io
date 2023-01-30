# Base Image
FROM python:3.9-alpine
#FROM pypy:3-onbuild

# create and set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

ADD  requirements.txt /code/requirements.txt

RUN apk update \
    && apk add \
    build-base \
    jpeg-dev \
    zlib-dev \
    python3-dev gcc musl-dev

RUN pip install --upgrade pip
RUN pip install virtualenv
RUN mkdir /python_virtualenv
RUN python3 -m venv /python_virtualenv/env
ENV source /python_virtualenv/env/bin/activate

RUN /python_virtualenv/env/bin/pip install flake8

RUN /python_virtualenv/env/bin/pip install -r requirements.txt
#ENTRYPOINT ["/python_virtualenv/env/bin/python", "manage.py"]
EXPOSE 8000
ENTRYPOINT ["/python_virtualenv/env/bin/python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
