# -*- coding:utf-8 -*-

__author__ = 'michael'

import models
from django.contrib import admin
from gallery.models import Gallery, News


class GalleryInline(admin.TabularInline):
	model = Gallery

class NewsInline(admin.TabularInline):
	model = News


class AdminChildPages(admin.ModelAdmin):
	inlines = [ GalleryInline, ]
        list_display = ('parent', 'title')
        list_display_links = list_display


class AdminNews(admin.ModelAdmin):
	inlines = [ NewsInline, ]

admin.site.register(models.ChildPages, AdminChildPages)
admin.site.register(models.ContactData)
admin.site.register(models.Main_imgs)
admin.site.register(models.News, AdminNews)
admin.site.register(models.Pages)
