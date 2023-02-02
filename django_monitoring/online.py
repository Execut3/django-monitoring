import datetime

from django.conf import settings

from .cache import CacheManager
from .consts import USER_ONLINE_CACHE_PREFIX


def get_online_users_id_list():
    """
    Return list of user id_list that visited any part of application
    within previous USER_ONLINE_TIMEOUT Minutes.
    """
    keys = CacheManager().get_keys_with_prefix(f'{USER_ONLINE_CACHE_PREFIX}*')
    id_list = [int(i.replace(USER_ONLINE_CACHE_PREFIX, '')) for i in keys]
    return id_list


def get_online_users__specific_datetime(date=None):
    """
    Get list of user_id_List which their last-seen is exactly in the date datetime(minute)
    """
    if not date:
        date = datetime.datetime.now()

    user_id_timestamp_dict = get_online_users_id_timestamp_dict()
    user_id_list = []
    for key, value in user_id_timestamp_dict.items():
        try:
            user_id = int(key.replace(USER_ONLINE_CACHE_PREFIX, ''))
        except:
            continue
        if not value and not user_id:
            continue
        if type(value) != datetime.datetime:
            continue
        diff = (date - value).seconds
        if diff <= 60:
            user_id_list.append(user_id)

    return user_id_list


def get_online_users_id_timestamp_dict():
    """
    will return a dict with keys:seen_<id> and values datetime.datetime objects
    """
    keys = CacheManager().get_keys_with_prefix(f'{USER_ONLINE_CACHE_PREFIX}*')
    item_dict = get_values
    item_dict = cache.get_many(keys)
    return item_dict


def user_last_seen(user_id):
    """
    Last seen datetime of user, return datetime object
    """
    return cache.get(f'{USER_ONLINE_CACHE_PREFIX}{user_id}', None)


def user_is_online(user_id):
    last_seen = user_last_seen(user_id)
    if not last_seen:
        return False
    now = datetime.datetime.now()
    return now <= last_seen + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)
