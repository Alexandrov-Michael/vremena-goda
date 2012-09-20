# -*- coding:utf-8 -*-

from django.db import models


class FormLog(models.Model):
    """
    loging form mail
    """

    email = models.EmailField(u'E-mail')
    date  = models.DateTimeField(u'Дата')
    text  = models.TextField(u'Содержание')

    def __unicode__(self):
        return u'%s %s' % (self.date, self.email)


    class Meta:
        verbose_name = u'Отправленное сообщения'
        verbose_name_plural = u'Отправленные сообещния'

