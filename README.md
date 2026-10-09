# Openstead Django starter

A minimal Django API with a private PostgreSQL connection and a database health
check. Create it from [Openstead](https://openstead.tech)'s Starter Projects
catalogue to configure the application and managed database together.

The catalogue generates `DJANGO_SECRET_KEY` and connects `DATABASE_URL` securely.
Complete the selected database and application service-month checkouts. The
application starts automatically after payment and database readiness.

For a repository deployment, set those two values in the service's secret
variables. Install with `pip install -r requirements.txt` and use
`gunicorn app:application --bind 0.0.0.0:$PORT` as the start command. The
application serves `/` and `/health`; the latter returns 503 when PostgreSQL
cannot be queried. Do not commit credentials or a local `.env` file.
