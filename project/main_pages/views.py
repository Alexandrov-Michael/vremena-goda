# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from models import Pages, ChildPages, News
from form_results.models import FormLog
from django.http import Http404
from forms import ContactForm


class PagesView(TemplateView):
    """
    view for all pages
    """

    child_page_template = 'child.html'

    def get_context_data(self, **kwargs):
        context = super(PagesView, self).get_context_data(**kwargs)
        page = self.get_page()
        context['page'] = page
        return context


    def get_page(self):
        """
        get page by url kwarg
        """
        url = self.kwargs.get('url', None)
        url = 'main' if not url else url
        try:
            page = Pages.objects.get(url=url)
            self.template_name = page.template
        except Pages.DoesNotExist:
            try:
                page = ChildPages.objects.get(url=url)
                self.template_name = self.child_page_template
            except ChildPages.DoesNotExist:
                raise Http404
        return page


pagesview = PagesView.as_view()






class NewsView(DetailView):
    """
    news views detail
    """
    model = News
    template_name = 'one_new.html'
    context_object_name = 'page'


newsview = NewsView.as_view()




class ContactView(FormView):
    """
    contact form view
    """
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = None

    def get_success_url(self):
        url = reverse('success', args=[])
        return url

    def form_valid(self, form):
        email = form.cleaned_data['email']
        text  = form.cleaned_data['text']
        new_obj = FormLog()
        new_obj.email = email
        new_obj.text = text
        new_obj.save()
        return super(ContactView, self).form_valid(form)

contactview = ContactView.as_view()





def success_view(request):
    """
    success view
    """
    return render(request, 'success.html', locals())


class NewsListView(ListView):
    """
    news list view
    """
    model = News
    template_name = 'news_list.html'
    paginate_by = 20
    context_object_name = 'news_list'

news_list_view = NewsListView.as_view()


