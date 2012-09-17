# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms

class ContactForm(forms.Form):
    """
    contact form
    """
    email = forms.EmailField(label=u'E-mail')
    text  = forms.CharField(label=u'Содержание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 20}))