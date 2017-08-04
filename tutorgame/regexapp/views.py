from django.shortcuts import render
def index(request):
    context_dict = {'viewmessage': 'this is a message from views.py'}
    return render(request, 'regexapp/index.html', context=context_dict)
# Create your views here.
