from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Card_Manager
#from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

    

def index(request, game_id):
    context_dict = {'viewmessage': 'this is a message from views.py'}
    cm = Card_Manager.objects.get(unique_id=game_id)
    return render(request, 'regexapp/index.html', context=context_dict)

def question_hw(request, game_id):
    cm = Card_Manager.objects.get(unique_id=game_id)
    cm.choose_node()
    repeat_me = cm.active_node.repeat_me
    data = {'repeat_me': repeat_me}
    return JsonResponse(data)
# Create your views here.

def new_game(request):
    game = Card_Manager()
    unique_id = game.unique_id
    return HttpResponseRedirect('/index/{}/'.format(unique_id))


'''
def check_homework(request):
'''  
