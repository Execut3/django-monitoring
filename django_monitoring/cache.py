from django.core.cache import cache


class CacheManager:

    def get_keys_with_prefix(self, prefix):
        return cache.keys(prefix)
