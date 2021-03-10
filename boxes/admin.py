from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Box, Member, Message


# With object permissions support
class BoxAdmin(GuardedModelAdmin):
    pass


admin.site.register(Box, BoxAdmin)
admin.site.register(Member)
admin.site.register(Message)
