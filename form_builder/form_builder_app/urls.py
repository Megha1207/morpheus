# form_builder_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('form/<int:form_id>/', views.fill_form, name='fill_form'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('analytics/<int:form_id>/', views.view_analytics, name='view_analytics'),
    path('forms/', views.form_list, name='form_list'),
]
