from django.conf import settings

USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

# Number of seconds of inactivity before a user is marked offline
USER_ONLINE_TIMEOUT = getattr(settings, 'USER_ONLINE_TIMEOUT', 300)

# Number of seconds that we will keep track of inactive users for before
# their last seen is removed from the cache
USER_LASTSEEN_TIMEOUT = getattr(settings, 'USER_LASTSEEN_TIMEOUT', 60 * 10)

# List of URLs to record request info. By default, will record all requests and responses.
RECORD_URLS = getattr(settings, 'RECORD_URLS', ['*'])
