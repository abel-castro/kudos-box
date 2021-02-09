from django import forms
from .models import Box, Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text', 'card_color', 'box')
        widgets = {'box': forms.HiddenInput()}


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('name', 'slug')