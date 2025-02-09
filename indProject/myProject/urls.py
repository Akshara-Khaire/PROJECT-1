from django.urls import path
from . import views

app_name = 'myProject'

urlpatterns = [
    path('project/', views.members , name = 'project' ),
]
