### DO NOT CLONE AND USE YET, Buggy and working on it


A Django App to deliver below features for better monitoring of services:

- Get online users
- Get last seen of each user (latest activity user did in the application)
- Get record of URL Attempts special login APIs to get a statistics of number of failed attempts for example
- Get response time of each URL


We recommended  use redis or memcache. And LocMemCache for local tests with bigger value of MAX_ENTRIES:
```python
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django-monitoring',
        'MAX_ENTRIES': 10000,
    }
}
```
