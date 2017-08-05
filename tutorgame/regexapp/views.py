from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    context_dict = {'viewmessage': 'this is a message from views.py'}
    return render(request, 'regexapp/index.html', context=context_dict)

def question_part_1(request):
    data = {'viewmessage': 'this is a message from views.py'}
    return JsonResponse(data)
# Create your views here.
