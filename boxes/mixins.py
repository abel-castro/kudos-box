from django.shortcuts import get_object_or_404
from django.urls import reverse
from guardian.shortcuts import get_objects_for_user

from .models import Box


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


class GetBoxMixin:
    def get_box(self):
        box_slug = self.kwargs.get("slug", None)
        return get_object_or_404(Box, slug=box_slug)
