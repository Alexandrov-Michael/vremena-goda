# -*- coding:utf-8 -*-

from django.db import models
from tinymce import models as tinymce_model


TEMPLATES_CHOICE = (
    ('main.html', 'Шаблон основной страницы'),
    ('child.html', 'Шаблон доп. страниц'),
)



class Pages(models.Model):
    """
    main pages model
    """

    title       = models.CharField(u'Заголовок', max_length=100)
    menu_title  = models.CharField(u'Название в меню', max_length=50)
    url         = models.CharField(u'Адрес', max_length=30, unique=True)
    template    = models.CharField(u'Шаблон', max_length=30, choices=TEMPLATES_CHOICE)
    menu_active = models.BooleanField(u'Активность в меню')
    body        = tinymce_model.HTMLField(u'Содержание', blank=True)
    menu_number = models.SmallIntegerField(u'Номер в меню', blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Основная страница'
        verbose_name_plural = u'Основные страницы'
	ordering = ['menu_number']


class ChildPages(models.Model):
    """
    model for child pages
    """
    parent      = models.ForeignKey(Pages, verbose_name=u'Родитель', related_name='rel_childs')
    url         = models.CharField(u'Адрес', max_length=30, unique=True)
    title       = models.CharField(u'Заголовок', max_length=100)
    menu_title  = models.CharField(u'Название в меню', max_length=50)
    menu_active = models.BooleanField(u'Активность в меню', default=True)
    main_page_menu_active = models.BooleanField(u'Отображение в меню на главной странице')
    body        = tinymce_model.HTMLField(u'Содержание', blank=True)
    order = models.PositiveIntegerField(u'Порядок')


    class Meta:
        verbose_name = u'Дополнительная страница'
        verbose_name_plural = u'Дополнительные страницы'
        ordering = ['order']


    def __unicode__(self):
        return u'%s' % (self.title)



class News(models.Model):
    """
    model for news
    """
    title  = models.CharField(u'Заголовок', max_length=100)
    date   = models.DateTimeField(u'Дата')
    active = models.BooleanField(u'Активность', default=True)
    body   = tinymce_model.HTMLField(u'Содержание')
    img    = models.ImageField('Логотип новости',upload_to='images', blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['-date']



class Main_imgs(models.Model):
    """
    model for main imgs
    """

    title = models.CharField(u'Заголовок', max_length=100)
    img   = models.ImageField(u'Картинка', upload_to='main_imgs')
    page  = models.ForeignKey(ChildPages, verbose_name=u'Ссылка на доп. страницу', related_name='rel_main_imgs')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Ссылка картинка на главной'
        verbose_name_plural = u'Ссылки картинки на главной'


class ContactData(models.Model):
    """
    models for contact data
    """
    name  = models.CharField(u'Наименование', max_length=50)
    value = models.CharField(u'Значение', max_length=300, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Контактные данные'
        verbose_name_plural = u'Контактные данные'

