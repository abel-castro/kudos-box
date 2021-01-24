from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'text', 'card_color', 'box')
        widgets = {'box': forms.HiddenInput()}

