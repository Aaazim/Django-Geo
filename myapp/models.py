from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
LANGUAGE_CHOICES = (
	('hi', 'Hindi'),
	('en', 'English')
	)
CURRENCY_CHOICES = (
	('USD', 'US Dollors'),
	('INR', 'Rupees')
	)

class Provider(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.IntegerField()
	language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
	currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

class ServiceAreas(models.Model):
	provider = models.ForeignKey(Provider)
	geo_json = models.PolygonField()