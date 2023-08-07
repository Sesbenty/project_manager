from api.views import *
from django.urls import path

urlpatterns = [
    path('tasks/', ListTask.as_view()),
    path('task/<str:pk>', DetailTask.as_view()),
    path('projects/', ListProject.as_view()),
    path('project/<str:pk>', DetailProject.as_view()),
]