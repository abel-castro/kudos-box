FROM python:3.9-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements

# install dependencies
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # project dependencies
  && apt-get install -y netcat git \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install --no-cache-dir -r /requirements/prod.txt

# copy files
COPY ./compose/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./compose/prod/start /start
RUN sed -i 's/\r//' /start && chmod +x /start

#create app user
RUN groupadd -r django && useradd --no-log-init -r -g django django
COPY --chown=django:django . /app/
RUN mkdir /app/staticfiles && chown django:django /app/staticfiles
# set container's default user
USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]