# form_builder_app/models.py
from django.db import models
import json

class Form(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('dropdown', 'Dropdown'),
        ('checkbox', 'Checkbox'),
    ]
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    options = models.TextField(blank=True, null=True)  # For Dropdown/Checkbox options
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text

class Response(models.Model):
    response_data = models.TextField()  # Stores response as a JSON string
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='responses')

    def save(self, *args, **kwargs):
        # Ensure response_data is in JSON format
        if isinstance(self.response_data, str):
            self.response_data = json.loads(self.response_data)
        super().save(*args, **kwargs)
