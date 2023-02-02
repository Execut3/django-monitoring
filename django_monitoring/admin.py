from django.contrib import admin

from .models import OnlineLog, URLRecord


class OnlineLogAdmin(admin.ModelAdmin):
    model = OnlineLog
    list_per_page = 20
    list_display = ('id', 'count', 'created_at',)


class URLRecordAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    search_fields = ('path', 'response_data', )
    list_filter = ('method', 'status_code', 'path', )
    list_display = ('id', 'path', 'duration', 'method', 'status_code', )


admin.site.register(OnlineLog, OnlineLogAdmin)
admin.site.register(URLRecord, URLRecordAdmin)
