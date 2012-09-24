# -*- coding:utf-8 -*-

__author__ = 'michael'

import models
from django.contrib import admin
from proj import settings
import os


class SliderAdmin(admin.ModelAdmin):
	list_display = (
		'get_img',
		'alt',
		'active',
	)
	list_display_links = ('get_img','alt',)
	list_editable = ('active',)

	def get_img(self, obj):
		image_path = os.path.join(settings.MEDIA_URL, obj.img.url)
		image_path = image_path.replace('\\','/') # Windows-Fix
		return '<a href="'+ str(obj.id) +'/"><img src="'+ str(image_path) +'" width="90" height="30" /></a>'
	
	get_img.short_description = 'Thumbnail'
	get_img.allow_tags = True


admin.site.register(models.SliderImgs, SliderAdmin)
