# -*- coding:utf-8 -*-

__author__ = 'michael'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wproduktru_vrem',                      # Or path to database file if using sqlite3.
        'USER': 'wproduktru_vrem',                      # Not used with sqlite3.
        'PASSWORD': 'vrem123456789',                  # Not used with sqlite3.
        'HOST': 'pg.sweb.ru',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}