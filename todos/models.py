# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Project(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField('Date started', default=timezone.now())

    def __unicode__(self):
        return self.title


#class Resource(models.Model):
#    RESOURCE_TYPES = (
#        'Image',
#        'Snippet',
#        'Link',
#        'Text',
#    )
#    project = models.ForeignKey(Project)
#    type = models.CharField(max_length=40, choices=RESOURCE_TYPES)
#    data = models.CharField(max_length=1000, blank=True)
#    pub_date = models.DateTimeField('Date added', default=timezone.now())
#
#    def __unicode__(self):
#        return self.data if self.data != "" else self.type


class Todo(models.Model):
    project = models.ForeignKey(Project)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date added', default=timezone.now())
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return ('✓ ' if self.completed else '') + self.description

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
