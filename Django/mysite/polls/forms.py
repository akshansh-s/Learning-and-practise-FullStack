from django import forms
from .models import Choice, Question

class VoteForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question_txt','pub_date']
        #date format is like- 2024-03-25 17:42:22
