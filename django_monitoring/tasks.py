import datetime

from .models import OnlineLog
from .online import get_online_users__specific_datetime


def update_online_logs():
    """
    Task to get list of online-user-idlist from cache
    and create a database instance to store the logs
    """
    now = datetime.datetime.now()
    user_id_list = get_online_users__specific_datetime(now)
    OnlineLog.objects.create(
        count=len(user_id_list),
        user_id_list=user_id_list,
    )
