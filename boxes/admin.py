from django.contrib import admin
from .models import Box, Member, Message
from guardian.admin import GuardedModelAdmin


# With object permissions support
class BoxAdmin(GuardedModelAdmin):
    pass


admin.site.register(Box, BoxAdmin)
admin.site.register(Member)
admin.site.register(Message)
