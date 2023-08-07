from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_request, name='login'),
    path('register', views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('projects', views.projects, name='projects'),
    path('project/<str:uuid>', views.project, name='project'),
    path('profile', views.profile, name='profile'),
    path('tasks', views.task_list, name='tasks'),
    path('users', views.user_list, name='users'),
    path('dashboard', views.dashboard, name='dashboard'),
]
