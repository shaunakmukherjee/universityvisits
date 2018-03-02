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
	url(r'^visitor$', views.Visitor.as_view()),
	url(r'^pending$', views.PendingVisits.as_view()),
	url(r'^guide1$', views.Guide1.as_view()),
	url(r'^guide2$', views.Guide2.as_view()),
	url(r'^guide3$', views.Guide3.as_view()),
	url(r'^guide4$', views.Guide4.as_view()),
	url(r'^guide5$', views.Guide5.as_view()),
	url(r'^guide6$', views.Guide6.as_view()),
	url(r'^history$',views.History.as_view()),
	url(r'^help$',views.Help.as_view()),
]
