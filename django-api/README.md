# Django-API

## connection between django and postgres

```
`settings.py`
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "coredb",
        "USER": "postgres",
        "PASSWORD": "password123!@#",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```

## Issue - Initial User Migration Failed with Admin.0001 Dependency

After creating the UserManager and User models, if the migration fails with the following error:
`Migration admin.0001_initial is applied before its dependency core_user.0001_initial on database 'default'.`

Please try running these commands:
`$ sudo su postgres`
`$ psql`
`postgres=# DROP DATABASE coredb;`
`postgres=# CREATE DATABASE coredb;`
`postgres=# ALTER ROLE core SET client_encoding TO 'utf8';`
`postgres=# ALTER ROLE core SET default_transaction_isolation TO 'read committed';`
`postgres=# ALTER ROLE core SET timezone TO 'UTC';`
`postgres=# ALTER DATABASE coredb OWNER TO core;`
`postgres=# GRANT ALL PRIVILEGES ON DATABASE coredb TO core;`

If you already ran the "makemigrations" for core_user, simply run `python manage.py migrate`
For more details check out this thread by our reader remyluslosius.

- DRF package installation `pip install djangorestframework django-filter`
- All requests that start with `'api/'` are referred to the URL configurations defined in `core.routers` module of the `core` app.
  `path('api/', include(("core.routers", "core"), namespace="core-api"))`
