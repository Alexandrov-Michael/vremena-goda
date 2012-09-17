# -*- coding:utf-8 -*-

from django.db import models
from main_pages.models import Pages, ChildPages


class SliderImgs(models.Model):
    """
    model for imgages slider
    """
    main_page  = models.ForeignKey(Pages, verbose_name=u'Отображение на основной странице', related_name='rel_main_page_slider', null=True, blank=True)
    child_page = models.ForeignKey(ChildPages, verbose_name=u'Отображение на доп. страницах', related_name='rel_child_page_slider', null=True, blank=True)
    for_all    = models.BooleanField(u'Отобразить на всех страницах')
    active     = models.BooleanField(u'Активность')
    img        = models.ImageField(u'Картинка', upload_to='images')
    desc       = models.CharField(u'Описание', max_length=150, blank=True)
    alt        = models.CharField(u'Описание если не доступна',max_length=100)

    def __unicode__(self):
        return self.alt

    class Meta:
        verbose_name = u'Картинка для слайдера'
        verbose_name_plural = u'Картинки для слайдера'
