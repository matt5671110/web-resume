from django.db import models

class Overview(models.Model):
	name = models.CharField(max_length=200)
	about = models.TextField('About Me')
	experience = models.TextField('Experience Description')
	education = models.TextField('Education Description')
	def __str__(self):
		return self.name

class Nickname(models.Model):
	nickname_text = models.CharField(max_length=200)
	def __str__(self):
		return self.nickname_text

class Job(models.Model):
	thumbnail = models.ImageField(upload_to='images/thumbnails/')
	cover_image = models.ImageField(upload_to='images/cover/')
	location = models.CharField('Where did you work',max_length=200)
	title = models.CharField('Job title',max_length=200)
	short_description = models.TextField('Short Description')
	complete_description = models.TextField('Complete Description')
	