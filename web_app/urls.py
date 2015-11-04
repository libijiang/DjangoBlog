from django.conf.urls import patterns, include, url
from django.contrib import admin
from os.path import join
import blog.views 


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','blog.views.entry',name='entry'),
    url(r'^blog/',include('blog.urls',namespace='blog')),
   	#url(r'^syncdb/', 'web_app.views.syncdb'),

	#ueditor
	url(r'^ueditor/',include('DjangoUeditor.urls')),
)
