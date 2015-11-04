from os import path
from django.db import models

class BL_article(models.Model):
	title=models.CharField(max_length=50)
	post_date=models.DateField(auto_now_add=True)
	date=models.ForeignKey('BL_date')
	tag=models.ManyToManyField('BL_tag')
	relate=models.ManyToManyField('BL_article',blank=True)
	content=models.TextField()
	describe=models.TextField()
	head_img=models.URLField()

	def __unicode__(self):
		return self.title



class BL_comment(models.Model):
	contant=models.TextField()
	article=models.ForeignKey('BL_article')
	author=models.CharField(max_length=50)
	date=models.DateField(auto_now_add=True)
	author_email=models.EmailField()
	author_ip=models.IPAddressField()
	reply=models.TextField(blank=True)
	isread=models.BooleanField(default=False)

	def __unicode__(self):
		return self.contant


class BL_tag(models.Model):
	name=models.CharField(max_length=50,unique=True)

	def __unicode__(self):
		return self.name


class BL_date(models.Model):
	date=models.DateField(unique=True)

	def __unicode__(self):
		return str(self.date.year)+'-'+str(self.date.month)


class BL_otherproj(models.Model):
	name=models.CharField(max_length=50)
	url=models.URLField()

	def __unicode__(self):
		return name










