from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, ListView

from kudosbox.settings import ADMIN_EMAIL
from .forms import MessageForm
from .models import Box, Message
from guardian.mixins import PermissionRequiredMixin


class HomeView(ListView):
    model = Box
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ADMIN_EMAIL'] = ADMIN_EMAIL
        return context


class BoxView(PermissionRequiredMixin, DetailView):
    model = Box
    template_name = 'box.html'
    permission_required = 'boxes.view_box'

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print('yes')
        return super(BoxView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages = Message.objects.filter(box=self.get_object())
        context['messages'] = messages
        return context


class CreateMessageView(CreateView):
    model = Message
    template_name = 'create_message.html'
    form_class = MessageForm

    def get_initial(self):
        initial = super().get_initial()
        initial['box'] = self.get_box_object().id
        return initial

    def get_box_object(self):
        box = get_object_or_404(Box, slug=self.kwargs['slug'])
        if not self.request.user.has_perm('boxes.view_box', box):
            raise PermissionDenied()
        return box

    def get_success_url(self):
        return f'/boxes/{self.get_box_object().slug}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box'] = self.get_box_object()
        return context
