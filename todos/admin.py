from django.contrib import admin
from todos.models import Todo, Project


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Todo info', {'fields': ['description', 'completed', 'project']})
    ]
    list_display = ('description', 'pub_date', 'completed', 'project')


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['start_date']}),
        ('Project info', {'fields': ['title', 'user']}),
        ]
    list_display = ('title', 'start_date', 'user')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Project, ProjectAdmin)