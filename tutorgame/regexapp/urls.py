from django.conf.urls import url
from regexapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/question_part_1/$', views.question_part_1, name='question_part_1'),
]
