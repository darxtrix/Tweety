from django.conf.urls import patterns, include, url
import views
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index),
    url(r'^index/$',views.index),
    url(r'^get_tweets/$',views.get_tweets),
)
