from django.conf.urls import patterns, include, url
from django.contrib import admin
from proj import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin_tools/',       include('admin_tools.urls')),
    url(r'^admin/doc/',         include('django.contrib.admindocs.urls')),
    url(r'^admin/',             include(admin.site.urls)),
    url(r'^tinymce/',           include('tinymce.urls')),
    url(r'^$',                  'main_pages.views.pagesview'),
    url(r'^gallery_main/$',     'main_gall.views.gallery_view', name='gallery'),
    url(r'^news_list/$',        'main_pages.views.news_list_view', name='news_list'),
    url(r'^news/(?P<pk>\d+)/$', 'main_pages.views.newsview'),
    url(r'^send_mail/$',        'main_pages.views.contactview', name='contact_mail'),
    url(r'^success/$',          'main_pages.views.success_view', name='success'),
    url(r'^(?P<url>.+)/$',      'main_pages.views.pagesview'),
)



if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
