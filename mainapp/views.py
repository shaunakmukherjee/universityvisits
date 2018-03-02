#mainapp/views.py


from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

class Parents(TemplateView):
	template_name = "parents.html"

class Visits(TemplateView):
	template_name = "visits.html"

class Becomeaguide(TemplateView):
	template_name = "become.html"

class Profile(TemplateView):
	template_name = "login.html"

class Policy(TemplateView):
	template_name = "policy.html"

class Visitor(TemplateView):
	template_name = "visitordash.html"

class PendingVisits (TemplateView):
	template_name = "pending.html"
