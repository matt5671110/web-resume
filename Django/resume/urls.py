from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('experience', views.experience, name='experience'),
	path('experience/project/<int:project_id>/', views.project_detail, name='project_detail'),
	path('experience/job/<int:job_id>/', views.job_detail, name='job_detail'),
	path('education', views.education, name='education'),
]