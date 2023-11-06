FROM python:3.12-slim

COPY . app/
WORKDIR /app
RUN apt update && apt install -y libpq-dev
RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8080

ENTRYPOINT [ "bin/entrypoint.sh" ]
