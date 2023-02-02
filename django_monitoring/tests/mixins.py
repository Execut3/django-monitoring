from unittest import TestCase

from django_monitoring.helpers import flush_cache


class CacheServiceTestMixin(TestCase):
    def setUp(self):
        super(CacheServiceTestMixin, self).setUp()
        self.clear_cache()

    def tearDown(self) -> None:
        super(CacheServiceTestMixin, self).tearDown()
        self.clear_cache()

    def clear_cache(self):
        flush_cache()
