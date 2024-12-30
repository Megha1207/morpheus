from django.contrib import admin

# Register your models here.
# form_builder_app/admin.py
from django.contrib import admin
from .models import Form, Question, Response

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class FormAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Form, FormAdmin)
admin.site.register(Question)
admin.site.register(Response)
