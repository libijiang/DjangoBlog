from django.conf.urls import patterns, include, url
from os.path import join


urlpatterns = patterns('',
    url(r'home/page_(?P<page_id>\d+)$','blog.views.home',name='home'),
    url(r'home/tag_(?P<tag_id>\d+)_page_(?P<page_id>\d+)$','blog.views.tag',name='tag'),
    url(r'home/archive_(?P<archive_date>\d+)_page_(?P<page_id>\d+)$','blog.views.archive_date',name='archive_date'),
    url(r'article_(?P<article_id>\d+)$','blog.views.article',name='article'),
    url(r'about$','blog.views.about',name='about'),

)
