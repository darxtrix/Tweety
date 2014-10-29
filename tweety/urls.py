from django.conf.urls import patterns, include, url
import views
from django.http import HttpResponse
from django.views.generic import TemplateView
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^get_tweets/$',views.get_tweets),
    url(r'^google4962e1a518060429\.html$', lambda r: HttpResponse("google-site-verification: google4962e1a518060429.html", mimetype="text/plain")), #added google site ownership verification file
	url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')), #added ronots.txt file
	url(r'^sitemap.xml$',TemplateView.as_view(template_name='sitemap.xml')), #serving sitemap
)
