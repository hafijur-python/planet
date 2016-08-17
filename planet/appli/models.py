from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Planets(models.Model):
	name = models.CharField( max_length=200)
	caption =models.CharField( max_length=200)
	temperature =models.IntegerField(default=0)
	radius = models.CharField(max_length=100)
	images = models.CharField(max_length=100, blank=True)
	detail = models.CharField( max_length=200)
	def __unicode__(self):
		return self.name
	   	# return "{0} {1} {2} {3} {4}".format(
     #        self, self.name, self.temperature, self.caption , self.radius,self.detail)
class Planet(models.Model):
	name = models.CharField( max_length=200)
	caption =models.CharField( max_length=200)
	temperature =models.IntegerField(default=0)
	radius = models.CharField(max_length=100)
	images = models.CharField(max_length=100, blank=True)
	detail = models.CharField( max_length=200)
	def __unicode__(self):
		return self.name