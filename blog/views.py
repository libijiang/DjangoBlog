	#coding:utf8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.core.urlresolvers import reverse
from blog import models
from django.template import Template,Context
from locale import atoi
from django.views.decorators.csrf import csrf_exempt
import string

############# tools ###############
def get_left_container_data():
	tags_list=[]
	dates_list=[]
	projs_list=[]

	tags=models.BL_tag.objects.all()
	dates=models.BL_date.objects.all()
	projs=models.BL_otherproj.objects.all()

	for tag in tags:
		if tag.bl_article_set.count()!=0:tags_list.append(tag)
	for date in dates:
		if date.bl_article_set.count()!=0:dates_list.append(date)

	return {'tags':tags_list,'dates':dates_list,'projs':projs_list}

def split_page(articles_count,page_id,page_size=6):
	page=articles_count/page_size
	print articles_count
	if not articles_count%page_size==0:page+=1
	pages=[i+1 for i in range(page)]
	page_id=atoi(page_id)

	if page_id-1<=page:
		start=page_size*(page_id-1)
		end=start+page_size
	else:
		start=0;end=page_size

	return {'pages':pages,'start':start,'end':end}

############# views ###############

def entry(request):
	return  HttpResponseRedirect(reverse('blog:home',args=[1]))

def home(request,page_id):

	articles_count=models.BL_article.objects.all().count()
	
	#get_split_page
	data=split_page(articles_count,page_id)
	articles=models.BL_article.objects.all()[data['start']:data['end']]
	contents={'current_page':string.atoi(page_id),'pages':data['pages'],'articles':articles}

	#get_left_data
	left_data=get_left_container_data()
	contents.update(left_data)

	return render(request,'home.html',contents)


def tag(request,tag_id,page_id):

	try:
		tag_choice=models.BL_tag.objects.get(id=tag_id)
		articles_count=tag_choice.bl_article_set.count()
	except models.BL_tag.DoesNotExist:
		raise Http404

	#get_split_page
	data=split_page(articles_count,page_id)
	articles=tag_choice.bl_article_set.all()[data['start']:data['end']]
	contents={'pages':data['pages'],'articles':articles,'tag_choice':tag_choice}

	#get_left_data
	left_data=get_left_container_data()
	contents.update(left_data)

	return render(request,'home.html',contents)


def archive_date(request,archive_date,page_id):
	try:
		date_choice=models.BL_date.objects.get(id=archive_date)
		articles_count=date_choice.bl_article_set.count()
	except models.BL_date.DoesNotExist:
		raise Http404

	#get_split_page
	data=split_page(articles_count,page_id)
	articles=date_choice.bl_article_set.all()[data['start']:data['end']]
	contents={'pages':data['pages'],'articles':articles,'date_choice':date_choice}

	#get_left_data
	left_data=get_left_container_data()
	contents.update(left_data)

	return render(request,'home.html',contents)

def article(request,article_id):
	try:
		article=models.BL_article.objects.get(id=article_id)
	except models.BL_article.DoesNotExist:
		raise Http404
				
	article_relates=article.relate.all()

	contents={'article':article,'next_article_id':atoi(article_id)+1,
	'previous_article_id':atoi(article_id)-1,'article_relates':article_relates}

	left_data=get_left_container_data()
	contents.update(left_data)

	try:
		article=models.BL_article.objects.get(id=atoi(article_id)+1)
	except models.BL_article.DoesNotExist:
		contents.pop('next_article_id')

	try:
		article=models.BL_article.objects.get(id=atoi(article_id)-1)
	except models.BL_article.DoesNotExist:
		contents.pop('previous_article_id')

	return render(request,'article.html',contents)	



def about(request):
	contents={}

	left_data=get_left_container_data()
	contents.update(left_data)

	return render(request,'about.html',contents)


	

