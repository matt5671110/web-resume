from django.contrib import admin

from .models import Overview, Nickname, Job, ExperienceBlurb, Project, Skill, ProjectPhoto, ProjectCategory

class SkillInline(admin.TabularInline):
	model = Skill
	extra = 3
class ProjectPhotoInline(admin.StackedInline):
	model = ProjectPhoto
	extra = 1

class ProjectAdmin(admin.ModelAdmin):
	inlines = [SkillInline, ProjectPhotoInline]

admin.site.site_title = 'Resume site administration'
admin.site.site_header = 'Resume Admin'
admin.site.register(Overview)
admin.site.register(Nickname)
admin.site.register(Job)
admin.site.register(ExperienceBlurb)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)