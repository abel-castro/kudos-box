FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

# install dependencies
RUN apt-get update \
&& apt-get install -y gcc python3-dev libpq-dev netcat\
    # Pillow dependencies
    #&& apt-get install jpeg-dev zlib-dev \
    && pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt \
    && apt-get clean && apt-get autoremove -y gcc


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
