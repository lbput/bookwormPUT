from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'apps.contact.views.contact_form', name='contact_form'),
    url(r'thank-you/$', 'apps.contact.views.thank_you', name='thank_you'),
)


