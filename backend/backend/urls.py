from django.urls import path
from privacy_filter import views

urlpatterns = [
    path('mark', views.mark_text, name='mark_text'),
    path('anonymize', views.anonymize_text, name='anonymize_text'),
]
