from django.conf.urls import patterns, url

from todos import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login', views.login_view, name='login_view'),
                       url(r'^logout', views.logout_view, name='logout_view'),
                       url(r'^register', views.register, name='register'),
                       url(r'^projects', views.projects, name='projects'),
                       url(r'^user/(?P<username>\w+)$', views.user, name="user"),
                       url(r'^todo/(?P<todo_id>\d+)/$', views.todo_detail, name='todo_detail'),
                       url(r'^project/(?P<project_id>\d+)/$', views.project_detail, name='project_detail'),
                       url(r'^submit_todo', views.submit_todo, name='submit_todo'),
                       url(r'^submit_project', views.submit_project, name='submit_project'),
                       url(r'^delete', views.delete, name='delete'),
                       url(r'^complete', views.complete, name='complete'),
                       )