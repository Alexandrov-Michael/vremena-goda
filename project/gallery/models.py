from django.db import models
from main_pages.models import ChildPages, News


class Gallery(models.Model):
	"""
	model for gallery for dop. pages
	"""
	parent = models.ForeignKey(ChildPages, related_name='rel_gallery_parent')
	img = models.ImageField(upload_to='images')

	def __unicode__(self):
		return u'%s' % (self.id,)


class News(models.Model):
	"""
	model for gallery for dop. pages
	"""
	parent = models.ForeignKey(News, related_name='rel_news_parent')
	img = models.ImageField(upload_to='images')

	def __unicode__(self):
		return u'%s' % (self.id,)
