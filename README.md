### DO NOT CLONE or USE THIS PACKAGE, Buggy and working on it


A Django App to deliver below features for better monitoring of services:

- Get online users
- Get last seen of each user
- Get record of URL Attempts special login APIs to get a statistics of number of failed attempts for example
- Get response time of each URL

This service use caching service for handling records of online users. 
I recommended  use redis or memcache. And LocMemCache for local tests with bigger value of MAX_ENTRIES:
```python
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'django-monitoring',
        'MAX_ENTRIES': 10000,
    }
}
```
