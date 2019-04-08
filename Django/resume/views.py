from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import Overview, Nickname

def index(request):
	overview = get_object_or_404(Overview, pk=1)
	nicknames = get_list_or_404(Nickname)
	return render(request, 'resume/index.html', {'overview': overview, 'nicknames': nicknames})