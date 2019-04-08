from django.contrib import admin

from .models import Overview, Nickname

admin.site.site_title = 'Resume site administration'
admin.site.site_header = 'Resume Admin'
admin.site.register(Overview)
admin.site.register(Nickname)