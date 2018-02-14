#mainapp/urls.py : defines URL's for the main site

from django.conf.urls import url
from mainapp import views

urlpatterns = [
   	url(r'^$', views.Home.as_view()),
    url(r'^parents$', views.Parents.as_view()),
	url(r'^visits$', views.Visits.as_view()),
	url(r'^become$', views.Becomeaguide.as_view()),
	url(r'^profile$', views.Profile.as_view()),
	url(r'^policy$', views.Policy.as_view()),

]
