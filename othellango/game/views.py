
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from . import game_handling

# Create your views here.

def game_index(request):
	return render(request, 'game/game_index.html')

def disk_moved(request):
	if request.method != 'POST':
		return HttpResponse(status=405)
	
	request.POST.get("title", "")
	

	responseData = {
        'next': 4,
        'name': 'Test Response',
        'roles' : ['Admin', 'User']
    }

	return JsonResponse(responseData)