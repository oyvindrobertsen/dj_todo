from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from todos.models import Todo, Project
from todos.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('todos:projects'))
    else:
        return render(request, 'todos/login_form.html')


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('todos:projects'))
    else:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('todos:index'))
        else:
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'todos/register_form.html', context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('todos:projects'))
        else:
            return HttpResponseRedirect(reverse('todos:index'))
    else:
        return HttpResponseRedirect(reverse('todos:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('todos:index'))


def user(request, username):
    u = User.objects.get(username=username)

    return render(request, 'todos/user.html')

@login_required
def projects(request):
    project_list = Project.objects.filter(user=request.user)
    context = {'project_list': project_list}
    r_context = RequestContext(request, context)
    return render(request, 'todos/projects.html', r_context)


@login_required
def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {'project': project}
    return render(request, 'todos/project_detail.html', context)


@login_required
def todo_detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    context = {'todo': todo}
    return render(request, 'todos/todo_detail.html', context)


@login_required
def submit_todo(request):
    if len(request.POST['description']) > 0:
        p = Project.objects.get(pk=request.POST['project_id'])
        p.todo_set.create(description=request.POST['description'])
        return HttpResponseRedirect(reverse('todos:projects'))
    else:
        return render(request, 'todos/projects.html', {
            'project_list': Project.objects.order_by('id'),
            'error_message': "Empty todos are illegal.",
        })


@login_required
def submit_project(request):
    if len(request.POST['title']) > 0:
        p = Project(title=request.POST['title'], user=request.user)
        p.save()
        return HttpResponseRedirect(reverse('todos:projects'))
    else:
        return render(request, 'todos/projects.html', {
            'project_list': Project.objects.order_by('id'),
            'error_message': "A project needs a title, silly.",
        })


@login_required
def delete(request):
    p = Todo.objects.get(pk=request.POST['id'])
    p.delete()
    return render(request, 'todos/projects.html', {
        'todo_list': Todo.objects.order_by('completed', 'id'),
    })


@login_required
def complete(request):
    p = Todo.objects.get(pk=request.POST['id'])
    p.completed = not p.completed
    p.save()
    return render(request, 'todos/projects.html', {
        'todo_list': Todo.objects.order_by('completed', 'id'),
    })
