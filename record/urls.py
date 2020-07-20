from django.urls import path, include
from .views import record, startRecording

urlpatterns = [
    path('', record, name= "record"),
    path('startRecording/', startRecording, name= "startRecording"),
]
