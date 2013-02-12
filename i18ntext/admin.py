# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Text #, Realm
from modeltranslation.admin import TranslationAdmin

#class RealmAdmin(admin.ModelAdmin):
#    search_fields = ('title', )
#    list_display = ('title', )
#    ordering = ('title', )
#
#admin.site.register(Realm, RealmAdmin)


class TextAdmin(TranslationAdmin):
    search_fields = ('title', 'key', 'text', )
    list_display = ('key', 'active', 'title', 'text', )
    ordering = ('title', 'key', 'text', )
    prepopulated_fields = {"key": ("title",)}

admin.site.register(Text, TextAdmin)
