# -*- coding:utf-8 -*-
from django.utils.functional import SimpleLazyObject
from main_pages.models import ContactData, Pages, ChildPages, Main_imgs, News
from slider.models import SliderImgs
from django.db.models import Q
__author__ = 'michael'


def contact_data(request):
    """
    processor for contact data
    """
    def get_contact_address():
        """
        for get contact data for lazy call
        """
        address, created = ContactData.objects.get_or_create(name=u'адрес')
        if created:
            address.value = u'Санкт-Петербург, ул. Стародеревенская, д. 33/10'
            address.save()
        return address.value

    def get_contact_metro():
        """
        get metro station
        """
        metro, created = ContactData.objects.get_or_create(name=u'метро')
        if created:
            metro.value = u'ст.м. "Комендантский проспект"'
            metro.save()
        return metro.value

    def get_contact_telefon():
        """
        get contact telefon
        """
        telefon, created = ContactData.objects.get_or_create(name=u'телефоны')
        if created:
            telefon.value = u'+7 (812) 601-81-80, 640-40-40'
            telefon.save()
        return telefon.value

    def get_contact_email():
        """
        get contact email
        """
        email, created = ContactData.objects.get_or_create(name='email')
        if created:
            email.value = u'info@vremena-goda-spb.ru'
            email.save()
        return email.value

    return {
        'address' : SimpleLazyObject(get_contact_address),
        'metro': SimpleLazyObject(get_contact_metro),
        'telefon': SimpleLazyObject(get_contact_telefon),
        'email': SimpleLazyObject(get_contact_email),
    }



def menu(request):
    """
    context processor for main menu
    """

    menu_items = Pages.objects.filter(menu_active=True)

    return {
        'menu_items' : menu_items,
    }



def slider(request):
    """
    slider context processor
    """

    path = request.path_info
    main_page = None
    child_page = None
    slider_for_all = None
    slider_for_page = None
    try:
        main_page = Pages.objects.get(url = path)
    except Pages.DoesNotExist:
        try:
            child_page = ChildPages.objects.get(url = path)
        except ChildPages.DoesNotExist:
            path = None
    if not path:
        slider_for_all = SliderImgs.objects.filter(for_all=True)
    if main_page or child_page:
        slider_for_page = SliderImgs.objects.filter(Q(main_page=main_page) | Q(child_page=child_page))
    return {
        'slider_for_all':slider_for_all,
        'slider_for_page':slider_for_page,
    }

def main_page_menu(request):
    """
    processor for main page menu
    """
    menu_item = ChildPages.objects.filter(main_page_menu_active=True)

    return {
        'main_page_menu_items': menu_item,
    }


def main_page_3_imgs(request):
    """
    main page imgs 3 items
    """
    imgs = Main_imgs.objects.all()[:3]

    return {
        'main_page_3_imgs': imgs,
    }

def main_news(request):
    """
    context processor for main list news
    """
    news = News.objects.all()[:4]
    return {
        'main_page_news': news,
    }
