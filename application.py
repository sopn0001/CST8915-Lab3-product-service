"""WSGI entry point for AWS Elastic Beanstalk.

The Python platform starts Gunicorn as `application:application` unless a
Procfile overrides it. This module exposes that callable.
"""
from app import app as application
