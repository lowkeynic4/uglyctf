#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
	name = models.CharField(max_length=200)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	active = models.IntegerField(default=1)
	require_regcodes = models.IntegerField(default=0)
	def __unicode__(self):
		return self.name

class Category(models.Model):
	game = models.ForeignKey(Game)
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Challenge(models.Model):
	game = models.ForeignKey(Game)
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=2000)
	points = models.IntegerField(default=100)
	active = models.IntegerField(default=0)
	key = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class Hint(models.Model):
	game = models.ForeignKey(Game)
	challenge = models.ForeignKey(Challenge)
	text = models.CharField(max_length=2000)
	active = models.IntegerField(default=0)
	def __unicode__(self):
		return self.text

class RegCodes(models.Model):
	code = models.CharField(max_length=200, null=True, blank=True)
	used = models.IntegerField(default=0)

	def __unicode__(self):
		return self.code

class Competitor(models.Model):
	game = models.ForeignKey(Game)
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=200)
	affiliation = models.CharField(max_length=200, null=True, blank=True)
	bad_keys = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	active = models.IntegerField(default=1)
	ipaddr = models.CharField(max_length=200, null=True, blank=True)
	regcode = models.ForeignKey(RegCodes, null=True)
	def __unicode__(self):
		return self.display_name

class Solved(models.Model):
	game = models.ForeignKey(Game)
	competitor = models.ForeignKey(Competitor)
	challenge = models.ForeignKey(Challenge)
	points = models.IntegerField(default=0)
	time = models.DateTimeField()

	

