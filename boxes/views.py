from basic_analytics_tracker.mixins import TrackingMixin
from guardian.mixins import PermissionRequiredMixin
from guardian.shortcuts import assign_perm

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, View

from boxes.forms import BoxForm, MessageForm
from boxes.mixins import BoxUrlMixin, GetBoxMixin
from boxes.models import Box, Message


class HomeView(TrackingMixin, BoxUrlMixin, ListView):
    model = Box
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ADMIN_EMAIL"] = settings.ADMIN_EMAIL
        return context


class ArchiveBoxMessagesView(PermissionRequiredMixin, GetBoxMixin, View):
    permission_required = "boxes.view_box"

    def dispatch(self, request, *args, **kwargs):
        box = self.get_box()
        Message.objects.filter(box=box).update(archived=True)
        return redirect(reverse_lazy("box_detail", kwargs={"slug": box.slug}))


class BoxDetailView(TrackingMixin, BoxUrlMixin, PermissionRequiredMixin, DetailView):
    model = Box
    template_name = "box.html"
    permission_required = "boxes.view_box"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = Message.objects.filter(box=self.get_object())
        messages_archived = messages.archived()
        messages_not_archived = messages.not_archived()
        context["messages_archived"] = messages_archived
        context["messages_not_archived"] = messages_not_archived
        return context


class BoxCreateView(TrackingMixin, BoxUrlMixin, CreateView):
    template_name = "box_create.html"
    model = Box
    form_class = BoxForm

    def form_valid(self, form):
        box = form.save()
        url = reverse_lazy("create_box_user", kwargs={"slug": box.slug})
        return HttpResponseRedirect(url)


class BoxUserCreateView(TrackingMixin, BoxUrlMixin, GetBoxMixin, CreateView):
    template_name = "box_user_create.html"
    model = User
    form_class = UserCreationForm

    def form_valid(self, form):
        box = self.get_box()
        user = form.save(commit=False)
        user.is_staff = True
        user.save()
        django_login_backend = "django.contrib.auth.backends.ModelBackend"
        login(self.request, user, backend=django_login_backend)

        demo_box, created = Box.objects.get_or_create(name="Demo", slug="demo")
        assign_perm("view_box", user, demo_box)
        assign_perm("view_box", user, box)
        url = reverse_lazy("box_detail", kwargs={"slug": box.slug})
        return HttpResponseRedirect(url)


class MessageCreateView(TrackingMixin, BoxUrlMixin, GetBoxMixin, CreateView):
    model = Message
    template_name = "message_create.html"
    form_class = MessageForm

    def get_initial(self):
        initial = super().get_initial()
        initial["box"] = self.get_box().id
        return initial

    def get_box(self):
        box = super().get_box()
        if not self.request.user.has_perm("boxes.view_box", box):
            raise PermissionDenied()
        return box

    def get_success_url(self):
        return reverse_lazy("box_detail", kwargs={"slug": self.get_box().slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box"] = self.get_box()
        return context
