import re
import logging
import datetime

from django.conf import settings
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

from .models import URLRecord
from .helpers import get_client_ip
from .consts import USER_ONLINE_CACHE_PREFIX


class ActiveUserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_user = request.user
        if request.user.is_authenticated:
            now = datetime.datetime.now()
            cache.set(f'{USER_ONLINE_CACHE_PREFIX}{current_user.id}', now, settings.USER_LASTSEEN_TIMEOUT)


# Make a regex that matches if any of our regexes match.
COMBINED_REGEX_URLS = "(" + ")|(".join(settings.RECORD_URLS) + ")"


class RecordURLMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super(RecordURLMiddleware, self).__init__(get_response)
        self.get_response = get_response

    def __call__(self, request):
        # Before the view is called
        path = request.path
        if re.match(COMBINED_REGEX_URLS, path):
            request.start_time = datetime.datetime.now()

        response = self.get_response(request)

        # After the view is called
        try:
            if re.match(COMBINED_REGEX_URLS, path):
                duration = (datetime.datetime.now() - request.start_time).total_seconds()
                ip_address = str(get_client_ip(request))
                user = request.user
                if not user.is_authenticated:
                    user = None
                URLRecord.objects.create(
                    path=path,
                    user=user,
                    ip=ip_address,
                    duration=duration,
                    method=request.method,
                    status_code=response.status_code,
                )
        except Exception as e:
            logging.error(str(e))

        return response
