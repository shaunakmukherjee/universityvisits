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

class Details(TemplateView):
	template_name = "details.html"

class GuideList(TemplateView):
	template_name = "guidelist.html"

class Policy(TemplateView):
	template_name = "policy.html"

class Visitor(TemplateView):
	template_name = "visitordash.html"

class PendingVisits (TemplateView):
	template_name = "pending.html"

class VisitHistory (TemplateView):
	template_name = "visithistory.html"

class GuideHistory (TemplateView):
	template_name = "guidehistory.html"

class Help (TemplateView):
	template_name = "helpcentre.html"
#functions for each of the guide signup steps

class Guide1(TemplateView):
	template_name = "guide1.html"
class Guide2(TemplateView):
	template_name = "guide2.html"
class Guide3(TemplateView):
	template_name = "guide3.html"
class Guide4(TemplateView):
	template_name = "guide4.html"
class Guide5(TemplateView):
	template_name = "guide5.html"
class Guide6(TemplateView):
	template_name = "guide6.html"
class Guide7(TemplateView):
	template_name = "guide7.html"
class Guide8(TemplateView):
	template_name = "guide8.html"

class BookConf2(TemplateView):
	template_name = "bookconf2.html"

class BookConf1(TemplateView):
	template_name = "bookconf1.html"
class GuideHome(TemplateView):
	template_name = "guidedash.html"
