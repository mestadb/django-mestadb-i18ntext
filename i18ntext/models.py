# -*- coding: utf-8 -*-

from django.db import models

#class Realm(models.Model):
#    title = models.CharField(max_length=255)
#
#    def __unicode__(self):
#        return self.title

class Text(models.Model):
    #realm = models.ForeignKey(Realm, editable=True, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, editable=True)
    key = models.SlugField(max_length=255, editable=True, unique=True, db_index=True)
    text = models.TextField(editable=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return u'%s' % (self.title)
