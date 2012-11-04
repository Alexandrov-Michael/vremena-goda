# -*- coding:utf-8 -*-
from django.db import models

class Gallery(models.Model):
    """
    Model for gallery jquery plugin
    """
    name = models.CharField(u'Название', max_length=100)
    title = models.CharField(u'Заголовок', max_length=100)
    alt = models.CharField(u'Описание', max_length=200)
    img = models.ImageField(u'Основная картинка', upload_to='gallery_main')
    thumb = models.ImageField(u'Миниатюра', upload_to='thumbs')
    caption = models.TextField(u'Описание под картинкой')
    order = models.PositiveIntegerField(u'Порядок')

    def __unicode__(self):
        return u'%s' % (self.id,)

    class Meta:
        verbose_name = u'Закладка галереи'
        verbose_name_plural = u'Закладка галереи'
        ordering = ['order']
