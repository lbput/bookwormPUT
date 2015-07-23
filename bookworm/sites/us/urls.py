from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static

from oscar.app import application
from oscar.views import handler500, handler404, handler403  # noqa

from paypal.express.dashboard.app import application as paypal
admin.autodiscover()

urlpatterns = [
    # Include admin as convenience. It's unsupported and you should
    # use the dashboard
    url(r'^admin/', include(admin.site.urls)),
    url(r'^checkout/paypal/', include('paypal.express.urls')),
    url(r'^dashboard/paypal/express/', include(paypal.urls)),
    # i18n URLS need to live outside of i18n_patterns scope of the shop
    # url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
    url(r'^contact/', include('apps.contact.urls', namespace='contact')),
]

# Prefix Oscar URLs with language codes
# urlpatterns += i18n_patterns('',
    ##Oscar's normal URLs
    # url(r'', include(application.urls)),
# )

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
