# -*- coding:utf-8 -*-

__author__ = 'michael'

import models
from django.contrib import admin
from gallery.models import Gallery


class GalleryInline(admin.TabularInline):
	model = Gallery


class AdminChildPages(admin.ModelAdmin):
	inlines = [ GalleryInline, ]

admin.site.register(models.ChildPages, AdminChildPages)
admin.site.register(models.ContactData)
admin.site.register(models.Main_imgs)
admin.site.register(models.News)
admin.site.register(models.Pages)
