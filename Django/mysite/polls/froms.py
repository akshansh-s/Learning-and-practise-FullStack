from django import forms
from .models import Choice

class VoteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
