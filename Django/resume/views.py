from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.db.models import F

from .models import Overview, Nickname, Job, ExperienceBlurb, ProjectCategory, Project, School

def index(request):
	overview = get_object_or_404(Overview, pk=1)
	nicknames = get_list_or_404(Nickname)
	return render(request, 'resume/index.html', {'overview': overview, 'nicknames': nicknames})

def experience(request):
	overview = get_object_or_404(Overview, pk=1)
	blurbs = ExperienceBlurb.objects.all()
	jobs = Job.objects.order_by(F('end_date').desc(nulls_first=True))
	project_categories = ProjectCategory.objects.all()
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

def education(request):
	overview = get_object_or_404(Overview, pk=1)
	schools = School.objects.order_by('-date_recieved')
	context = {
		'overview': overview,
		'schools': schools,
	}
	return render(request, 'resume/education.html', context)

def project_detail(request, project_id):
	overview = get_object_or_404(Overview, pk=1)
	project = get_object_or_404(Project, pk=project_id)
	context = {
		'overview': overview,
		'project': project,
	}
	return render(request, 'resume/project_detail.html', context)

def job_detail(request, job_id):
	overview = get_object_or_404(Overview, pk=1)
	job = get_object_or_404(Job, pk=job_id)
	context = {
		'overview': overview,
		'job': job,
	}
	return render(request, 'resume/job_detail.html', context)