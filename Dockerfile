FROM python:3.12-slim

ARG SECRET_KEY
ARG DEBUG="True"
ARG POSTGRES_PASSWORD
ARG POSTGRES_USER
ARG POSTGRES_PORT="5432"
ARG POSTGRES_DB="vegetation_db"
ARG POSTGRES_HOST

COPY . app/
WORKDIR /app
RUN apt update && apt install -y libpq-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN touch .env \
    && echo SECRET_KEY=${SECRET_KEY} >> .env \
    && echo DEBUG=${DEBUG} >> .env \
    && echo POSTGRES_PASSWORD=${POSTGRES_PASSWORD} >> .env \
    && echo POSTGRES_USER=${POSTGRES_USER} >> .env \
    && echo POSTGRES_PORT=${POSTGRES_PORT} >> .env \
    && echo POSTGRES_DB=${POSTGRES_DB} >> .env \
    && echo POSTGRES_HOST=${POSTGRES_HOST} >> .env

EXPOSE 8080

ENTRYPOINT [ "bin/entrypoint.sh" ]
