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
	thumbnail = models.ImageField(upload_to='images/thumbnails/', blank=True)
	cover_image = models.ImageField(upload_to='images/cover/', blank=True)
	location = models.CharField('Where did you work',max_length=200)
	title = models.CharField('Job title',max_length=200)
	start_date = models.DateField('Start Date',null=True)
	end_date = models.DateField('End Date',help_text="Leave empty if still working",blank=True,null=True)
	short_description = models.TextField('Short Description', blank=True)
	complete_description = models.TextField('Complete Description', blank=True)
	def __str__(self):
		return self.location

class ExperienceBlurb(models.Model):
	blurb_text = models.CharField('Experience Text',max_length=200)
	def __str__(self):
		return self.blurb_text

class ProjectCategory(models.Model):
	name = models.CharField('Category Name', max_length=200)
	def __str__(self):
		return self.name

class Project(models.Model):
	category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True)
	thumbnail = models.ImageField(upload_to='images/thumbnails/', blank=True)
	name = models.CharField('Project Name',max_length=200)
	has_source = models.BooleanField('Has Source Code?',default=True)
	source_url = models.URLField('Source Code URL',max_length=1000,null=True,blank=True)
	source_link_text = models.CharField(max_length=200, default='Github')
	short_description = models.TextField('Short Description', blank=True)
	complete_description = models.TextField('Complete Description', blank=True)
	def __str__(self):
		return self.name

class Skill(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	skill = models.CharField(max_length=200)
	def __str__(self):
		return self.skill

class ProjectPhoto(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='images/photos/')

class School(models.Model):
	thumbnail = models.ImageField(upload_to='images/thumbnails/', blank=True)
	institution = models.CharField(max_length=200)
	earned = models.CharField('What did you earn',help_text="Diploma, Degree, Certification, etc.",max_length=200)
	date_recieved = models.DateField('Date Recieved',help_text="Put expected date if not yet recieved")
	def __str__(self):
		return self.institution