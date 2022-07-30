from django import forms
from django.forms import widgets

from webapp.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]



class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["text_var", "interview"]
        widgets = {
            "interview": widgets.Select
        }





