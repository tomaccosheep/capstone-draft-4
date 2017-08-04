from django.conf.urls import url
from regexapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
