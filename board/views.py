from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.formats import localize

from .forms import NewUserForm, UpdateUserForm


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def user_list(request):
    users = User.objects.all()
    t_dict = []
    for t in users:
        a = {
            'first_name': str(t.first_name),
            'last_name': str(t.last_name),
            'email': str(t.email),
            'position': '',
            'last_login': str(localize(t.last_login))
        }
        t_dict.append(a)
    return render(request, 'users.html', {'users': t_dict})


@login_required
def task_list(request):
    all_tasks = []
    t_list = request.user.tasks.all()
    for t in t_list:
        t_dict = {
            'uuid': str(t.uuid),
            'name': t.name if t.name is not None else 'Без названия',
            'boardName': t.boardName,
            'date': str(localize(t.date))
        }
        all_tasks.append(t_dict)
    return render(request, 'task_list.html', {'tasks': all_tasks})


@login_required
def projects(request):
    projects = []
    t_list = request.user.projects.all()
    for t in t_list:
        t_dict = {
            'uuid': str(t.uuid),
            'name': str(t.name),
            'date': str(localize(t.date)),
            'owner': str(t.owner),
        }
        projects.append(t_dict)
    return render(request, 'projects.html', {'projects': projects})


@login_required
def project(request, uuid):
    t = request.user.projects.filter(uuid=uuid).first()
    t_dict = {
        'uuid': str(t.uuid),
        'name': str(t.name),
        'date': str(localize(t.date)),
        'owner': str(t.owner),
    }
    tasks = []
    t_tasks = t.tasks.all()
    for i in t_tasks:
        a = {
            'uuid': str(i.uuid),
            'name': i.name if i.name is not None else 'Без названия',
            'boardName': i.boardName,
            'date': str(localize(i.date)),
            'owner': {
                'full_name': i.owner.last_name + ' ' + i.owner.first_name,
            }
        }
        tasks.append(a)
    users = User.objects.all()
    return render(request, 'project.html', {'project': t_dict, 'tasks': tasks, 'users': users})


@login_required
def home(request):
    all_tasks = []
    t_list = request.user.tasks.all()
    for t in t_list:
        t_dict = {
            'uuid': str(t.uuid),
            'name': t.name if t.name is not None else 'Без названия',
            'boardName': t.boardName,
            'date': str(localize(t.date))
        }
        all_tasks.append(t_dict)
    return render(request, 'index.html', {'tasks': all_tasks})


def profile(request):
    form = UpdateUserForm()
    return render(request, 'profile.html', context={'login_form': form})


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,
                             'Аккаунт зарегистрирован: '
                             'добро пожаловать на сайт!')
            return redirect('board:login')
        messages.error(request, 'Не удалось зарегистрировать аккаунт. '
                                'Проверьте корректность данных и '
                                'попробуйте еще раз!')
    form = NewUserForm()
    return render(request=request,
                  template_name='register.html',
                  context={'register_form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,
                              f'Вы вошли на сайт под ником {username}.')
                return redirect('board:home')
            else:
                messages.error(request, 'Неверные имя и/или пароль.')
        else:
            messages.error(request, 'Неверные имя и/или пароль.')
    form = AuthenticationForm()
    return render(request=request, template_name='login.html',
                  context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Вы вышли из аккаунта.')
    return redirect('board:login')
