# -*- coding:utf-8 -*-
from django.contrib import admin
import models


class FormLogAdmin(admin.ModelAdmin):
	list_display = ('date', 'email')

admin.site.register(models.FormLog, FormLogAdmin)
