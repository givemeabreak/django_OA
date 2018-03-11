"""
Django settings for django_OA project.

Generated by 'django-admin startproject' using Django 2.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Default settings
# Shared settings between development and production

if os.environ.get('DJANGO_RELEASE_SETTINGS', None):
    from .rel_settings import *
else:
    from .dev_settings import *


