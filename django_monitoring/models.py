from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class OnlineLogManager(models.Manager):

    def distinct_users(self, **kwargs):
        qs = self.all()
        date = kwargs.get('date', None)
        if date:
            qs = qs.filter(created_at__date=date)
        hour = kwargs.get('hour', None)
        if hour != None:    # if 0 also ok, be note that.
            qs = qs.filter(created_at__hour=hour)

        qs = qs.filter(count__gt=1)
        user_id_list_list = qs.values_list('user_id_list', flat=True)
        user_id_list = []
        for item in user_id_list_list:
            for user_id in item:
                if not user_id in user_id_list:
                    user_id_list.append(user_id)

        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.filter(id__in=user_id_list).distinct()


class OnlineLog(models.Model):
    data = models.JSONField(
        null=True,
        blank=True,
        default=dict,
        verbose_name='List of online users'
    )   # Can be null, cause maybe that moment there is no user online
    count = models.IntegerField(
        default=0,
        verbose_name='Count of Online users'
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = OnlineLogManager()

    def __str__(self):
        return f'{self.created_at}, {self.count}'

    @property
    def user_id_list(self):
        return getattr(self.data, 'user_id_list', [])


class URLRecord(models.Model):
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Request User'
    )
    path = models.CharField(
        max_length=255,
        verbose_name='Request URL Path'
    )
    method = models.CharField(
        max_length=10,
        verbose_name='Request Method'
    )
    status_code = models.IntegerField()
    request_data = models.TextField(
        blank=True,
        default='',
    )
    response_data = models.TextField(
        blank=True,
        default='',
    )
    duration = models.FloatField(
        null=True,
        verbose_name='Duration of each request (ms)'
    )
    ip = models.CharField(
        null=True,
        blank=True,
        max_length=16,
        verbose_name="IP",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path

    def save(self, *args, **kwargs):
        if self.path:
            self.path = self.path[:255]
        if self.request_data:
            self.request_data = self.request_data[:1000]
        return super(URLRecord, self).save(*args, **kwargs)
