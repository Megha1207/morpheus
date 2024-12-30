# form_builder_app/forms.py
from django import forms
from .models import Question

class FormCreationForm(forms.Form):
    title = forms.CharField(max_length=100)
    questions = forms.JSONField()

class ResponseForm(forms.Form):
    # Dynamically add fields for each question based on the form provided
    pass
