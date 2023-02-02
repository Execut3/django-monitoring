import logging

from django.core.cache import cache


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def delete_cache(cache_key):
    try:
        cache.delete_many(keys=cache.keys(cache_key))
    except Exception as e:
        logging.error(str(e))


def flush_cache():
    try:
        for key in list(cache.keys('*')):
            cache.delete(key.replace(':1:', ''))
    except AttributeError as e:
        if 'LocMemCache' in str(e):
            # Using LocMemCache, so handle it
            print('locmem')