# -*- coding:utf-8 -*-
from main_gall import models
from django.shortcuts import render

def gallery_view(request):
    """
    View for render gallery
    """
    #template = 'gallery_base.html'
    template = 'gallery2.html'
    gallery_set = models.Gallery.objects.all()
    return render(request, template, locals())
