from django.contrib import admin
from todos.models import Todo, Project


class TodoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Todo info', {'fields': ['description', 'completed']})
    ]
    list_display = ('description', 'pub_date', 'completed')


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date information', {'fields': ['start_date']}),
        ('Project info', {'fields': ['title']}),
        ]

admin.site.register(Todo, TodoAdmin)