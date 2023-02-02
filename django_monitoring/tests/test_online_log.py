import datetime

from django.contrib.auth import get_user_model
from django.core.cache import cache

from .mixins import CacheServiceTestMixin
from ..models import OnlineLog
from ..tasks import update_online_logs

User = get_user_model()


class OnlineLogTest(CacheServiceTestMixin):

    def test_check_redis_integration(self):
        """
        Simple test to just check if redis is on
        and integration with caching system is enabled.
        """
        key = 'testkeyforredischecking'
        value = 'testvalue'
        cache.set(key, value)

        x = cache.get(key)
        self.assertEqual(x, value)

    def test_create_online_log(self):
        self.clear_cache()
        cache.set('seen_1', datetime.datetime.now())
        cache.set('seen_2', datetime.datetime.now())
        self.assertEqual(OnlineLog.objects.count(), 0)

        update_online_logs()
        log = OnlineLog.objects.first()
        self.assertTrue(log)
        self.assertEqual(log.count, 2)
        self.assertTrue(1 in log.user_id_list)
        self.assertTrue(2 in log.user_id_list)

    def test_distinct_users_manager(self):
        user1 = User.objects.create(username='u1')
        user2 = User.objects.create(username='u2')
        user3 = User.objects.create(username='u3')
        user4 = User.objects.create(username='u4')

        now = datetime.datetime.now()
        date = now - datetime.timedelta(minutes=2)
        OnlineLog.objects.create(user_id_list=[user1.id, user2.id], count=2, created_at=date)

        date = now - datetime.timedelta(minutes=4)
        OnlineLog.objects.create(user_id_list=[user1.id, user4.id], count=2, created_at=date)

        users = OnlineLog.objects.distinct_users(date=datetime.datetime.now().date())
        self.assertIn(user1, users)
        self.assertIn(user2, users)
        self.assertIn(user4, users)
        self.assertNotIn(user3, users)
