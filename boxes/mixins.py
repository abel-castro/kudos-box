from django.urls import reverse
from guardian.shortcuts import get_objects_for_user


class BoxUrlMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            box = (
                get_objects_for_user(self.request.user, "boxes.view_box")
                .exclude(slug="demo")
                .first()
            )
            if box:
                context["box_url"] = reverse("box_detail", kwargs={"slug": box.slug})
        return context
