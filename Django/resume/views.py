from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext

from .models import Overview, Nickname, Job, ExperienceBlurb, ProjectCategory, Project

def index(request):
	overview = get_object_or_404(Overview, pk=1)
	nicknames = get_list_or_404(Nickname)
	return render(request, 'resume/index.html', {'overview': overview, 'nicknames': nicknames})

def experience(request):
	overview = get_object_or_404(Overview, pk=1)
	blurbs = ExperienceBlurb.objects.all
	jobs = Job.objects.all
	project_categories = ProjectCategory.objects.all
	num_categories_with_projects = 0
	for category in ProjectCategory.objects.all():
		if category.project_set.count() > 0:
			num_categories_with_projects = num_categories_with_projects + 1
	context = {
		'overview': overview,
		'blurbs': blurbs,
		'jobs': jobs,
		'categories': project_categories,
		'num_categories_with_projects': num_categories_with_projects,
	}
	return render(request, 'resume/experience.html', context)