#coding:utf8
from django.contrib import admin
from blog import models
from django import forms
from DjangoUeditor.widgets import UEditorWidget
from web_app.settings import MEDIA_ROOT
import datetime
from sae.storage import Bucket
import re
from django.db.models.signals import m2m_changed  


class BL_article_AdminForm(forms.ModelForm):
	class Meta:
		model=models.BL_article
		fields=('title','describe','content','tag')
		widgets={
			'content':UEditorWidget(attrs={'width':1000, 'height':300, 
				'toolbars':'besttome',
				'imagePath':u'%(date)s_%(rnd)s.%(extname)s', 
				'filePath':u'%(date)s_%(rnd)s.%(extname)s', 
				'upload_settings':{'imageMaxSize':1204000}} ),
			'describe':UEditorWidget(attrs={'width':1000, 'height':300, 
				'toolbars':'besttome',
				'imagePath':u'%(date)s_%(rnd)s.%(extname)s', 
				'filePath':u'%(date)s_%(rnd)s.%(extname)s', 
				'upload_settings':{'imageMaxSize':1204000}} ),
		}


class BL_article_Admin(admin.ModelAdmin):
	fields=('title','describe','content','tag')
	filter_horizontal = ('tag',)
	form=BL_article_AdminForm


	def save_model(self,request, obj, form, change):

		#处理head_img
		img_pattern=re.compile(r'<img src="([^"]+)"')
		img_url=img_pattern.search(obj.describe+obj.content)
		if img_url: obj.head_img=img_url.groups()[0]

		#处理data和post_date
		now=datetime.datetime.now()
		obj.post_date=now
		try:
			bl_date=models.BL_date.objects.get(date__year=now.year,date__month=now.month)	
		except models.BL_date.DoesNotExist:
			date=models.BL_date(date=obj.post_date)
			date.save()
			obj.date=date
		else:
			obj.date=bl_date

		super(BL_article_Admin,self).save_model(request,obj,form,change)
	

class BL_comment_Admin(admin.ModelAdmin):
	pass
class BL_tag_Admin(admin.ModelAdmin):
	pass
class BL_date_Admin(admin.ModelAdmin):
	pass
class BL_otherproj_Admin(admin.ModelAdmin):
	pass



# Register models here.
admin.site.register(models.BL_article,BL_article_Admin)
admin.site.register(models.BL_comment,BL_comment_Admin)
admin.site.register(models.BL_tag,BL_tag_Admin)
admin.site.register(models.BL_date,BL_date_Admin)
admin.site.register(models.BL_otherproj,BL_otherproj_Admin)


############# set article relate ###############
def get_article_relate(article):

	tags=set(article.tag.all())
	articles=models.BL_article.objects.exclude(id=article.id)
	result=[]

	for article in articles:
		similitude=len(set(article.tag.all()) & tags)
		if similitude:result.append((article,similitude))

	return [item[0] for item in sorted(result,key=lambda a:a[1],reverse=True)][:4]


def set_relate_article(sender,instance,action,reverse,model,pk_set,**kwargs):
	if action=="post_add" and isinstance(instance, models.BL_article) and model==models.BL_tag:
		articles=get_article_relate(instance)
		instance.relate.clear()
		instance.relate.add(*articles)
		instance.save()


m2m_changed.connect(set_relate_article)