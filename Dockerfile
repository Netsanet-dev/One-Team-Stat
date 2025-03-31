# Stage 1
FROM python:3.12.3-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev postgresql-client && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.12.3-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY --from=builder /app/ .

COPY . /app/

COPY gunicorn.conf.py /app/

RUN pip freeze


# Port 8000 is exposed because it is the default port for the Gunicorn server
# and aligns with the application's configuration for serving HTTP requests.
EXPOSE 8000

# Gunicorn is used as the WSGI HTTP server to serve the Django application in production.
# The --bind option specifies the network interface and port for the server to listen on.
CMD ["gunicorn",  "-c", "gunicorn.conf.py" , "OneTeamStat.wsgi:application"]
