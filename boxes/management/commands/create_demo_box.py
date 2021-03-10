from django.core.management.base import BaseCommand, CommandError
from guardian.shortcuts import assign_perm
from guardian.utils import get_anonymous_user

from boxes.models import Box


class Command(BaseCommand):
    help = "Creates a new demo box."

    def handle(self, *args, **options):
        new_box, created = Box.objects.get_or_create(name="Demo", slug="demo")
        anonymous_user = get_anonymous_user()
        if created:
            assign_perm("view_box", anonymous_user, new_box)
            print(
                f"A new demo box was created! The box can viewed here: /boxes/{new_box.slug}"
            )
        else:
            print(
                f"The box already exists. The box can viewed here: /boxes/{new_box.slug}"
            )
